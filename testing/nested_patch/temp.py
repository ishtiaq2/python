# Assert SSH and Web Connection Methods:
# -------------------------------------
# Assert that with mocking 'mavencommlib.webcall_json', No Exception happens
# Mock both SSH and WEB without Exception
with mock.patch('maven_dut.SshConnection') as mock_Ssh_call:
with mock.patch('maven_dut.Dut') as mock_dut_call:
with mock.patch('mavencommlib.webcall_json') as mock_node_call:
sn.ssh_web_connection()

# Mock SSH without and WEB with Exception
with pytest.raises(RuntimeError) as excinfo:
with mock.patch('maven_dut.SshConnection') as mock_Ssh_call:
with mock.patch('mavencommlib.webcall_json', side_effect=[Exception("Failed to access web")]) \
as mock_node_call:
sn.ssh_web_connection()
# Assert that correct Exception is raised
assert 'Connection Error' in excinfo.value.message

# Mock SSH with Exception and WEB without
with pytest.raises(RuntimeError) as excinfo:
with mock.patch('maven_dut.SshConnection', side_effect=[Exception("Failed to access SSH_connection")]) \
as mock_Ssh_call:
with mock.patch('mavencommlib.webcall_json') as mock_node_call:
sn.ssh_web_connection()
# Assert that correct Exception is raised
assert 'Connection Error' in excinfo.value.message

# Print the functions which are mocked
print mock_node_call.call_args_list
# assert 1 == 0

# CONNECT
# ----------
# Mock SSH_Web_Connection Method:
assert sn.soak_stage == SoakStage.CONNECT
assert sn.conn_done == False
# This one is NOT successful
with mock.patch.object(SoakNode, 'ssh_web_connection',
side_effect=mocked_spend_time)as mocked_ssh_web_call:
# side_effect=Exception("Things went bad")]
with mock.patch('monotonic.monotonic', side_effect=mocked_monotonic):
sn.update()
# assert sn.soak_stage == SoakStage.CONNECT
assert sn.soak_stage == SoakStage.ABORTED
assert sn.conn_done == False
def ssh_web_connection(self):
try:
ssh_connection = maven_dut.SshConnection(self.ip_address)
self.dut = maven_dut.Dut(ssh_connection)
self.node_serial_number = self.dut.serial
self.node_article_number = self.dut.art_no
self.node_system_uptime = int(self.dut.uptime)

mavencommlib.webcall_json("https://{}/api/get_all_nodes".format(self.ip_address))
self.conn_done = True
except Exception:
self.conn_done = False
self.logger.exception("Exception while connecting")
raise RuntimeError("Connection Error {}....!".format(self.ip_address))
def update(self, verbose=True):
# CONNECT:
# If ping is successful ---> try ssh and web connection:
if self.soak_stage == SoakStage.CONNECT:
# If connection is successful - ssh thingies, go to INITIALIZE
# try:
##################################333
print 'hI'
start = monotonic.monotonic()
t = monotonic.monotonic() - start

while monotonic.monotonic() - start < 120 and self.conn_done == False:
try:
self.ssh_web_connection()
except Exception:
self.logger.exception('Failed to connect to Node {}'.format(self.ip_address))
if monotonic.monotonic() - start >= 120:
self.soak_stage = SoakStage.ABORTED
break
'''
while monotonic.monotonic() - start > 120 and self.conn_done == False:
self.soak_stage = SoakStage.ABORTED
break
print 'test ...'
try:
self.ssh_web_connection()
except Exception:
self.logger.exception('Failed to connect to Node {}'.format(self.ip_address))
print 'hI ...'
'''
#########################################3
if self.conn_done == True:
self.conn_done = False
print 'bye'
self.ssh_web_connection()
self.number_of_alarms = self.read_number_of_alarms()
if self.number_of_alarms != 0:
self.soak_stage = SoakStage.ABORTED
else:
try:
# Update db with parameters from SSh_conn.
statement = "UPDATE SoakNodes SET NodeUptime = ?, NodeSerial = ?, NodeArticleNumber = ? " \
"WHERE IPAddress = ?"
if verbose is True:
self.logger.debug("Executing SQL: {}".format(statement))
self.soak_db.execute(statement,
(self.node_system_uptime, self.node_serial_number,
self.node_article_number, self.ip_address))
self.soak_db.commit()
except Exception:
self.logger.exception("Failed to update database with values received from SSH_Connection!")
self.soak_stage = SoakStage.INITIALIZE
# except Exception:
# TODO: If we have tried for more than 120 seconds to log in, abort
# self.logger.exception('Failed to connect to Node {}'.format(self.ip_address))

# INITIALIZE:
elif self.soak_stage == SoakStage.INITIALIZE:
# update database with number of alarms
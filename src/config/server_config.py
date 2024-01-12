# wsadmin script generated by binaryAppScanner
# This configuration was migrated on 5/5/21 at 11:50:54 AM from the following location: /opt/IBM/WebSphere/AppServer/profiles/AppSrv01
# The binary scanner does not support the migration of all WebSphere traditional configuration elements. Check the binary scanner documentation for the list of supported configuration elements.

Cell=AdminConfig.getid('/Cell:' + AdminControl.getCell() + '/')
Node=AdminConfig.getid('/Cell:' + AdminControl.getCell() + '/Node:' + AdminControl.getNode() + '/')
Server=AdminConfig.getid('/Cell:' + AdminControl.getCell() + '/Node:' + AdminControl.getNode() + '/Server:server1')
NodeName=AdminControl.getNode()

print 'Starting Creating JVM Properties'
# Properties are migrated from server workstationNode01/server1.

print 'Starting Creating Authentication Alias'

print 'Starting Creating Queues'

print 'Starting Creating Topics'

print 'Starting Creating Activation Specifications'

print 'Starting Creating Connection Factories'

print 'Starting Creating JDBC Providers'
AdminConfigVar_0=AdminConfig.create('JDBCProvider', Node, [['name', 'Derby_JDBC_Provider'], ['implementationClassName', 'org.apache.derby.jdbc.EmbeddedConnectionPoolDataSource'], ['providerType', 'Derby JDBC Provider'], ['description', 'Derby embedded non-XA  JDBC Provider'], ['classpath', '${DERBY_JDBC_DRIVER_PATH}/derby.jar'], ['xa', 'false']])
AdminConfigVar_1=AdminTask.createDatasource(AdminConfigVar_0, ["-name", "Default Datasource", "-jndiName", "DefaultDatasource", "-dataStoreHelperClassName", "com.ibm.websphere.rsadapter.DerbyDataStoreHelper", "-configureResourceProperties", "[[databaseName java.lang.String ${APP_INSTALL_ROOT}/${CELL}/defaultapplication.war/DefaultDB] ]"])
AdminConfigVar_2=AdminConfig.showAttribute(AdminConfigVar_1, 'propertySet')
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'connectionAttributes'], ['type', 'java.lang.String'], ['value', 'upgrade=true']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'name'], ['type', 'java.lang.String'], ['value', 'Default Datasource']])
AdminConfigVar_3=AdminConfig.showAttribute(AdminConfigVar_1, 'connectionPool')
AdminConfig.modify(AdminConfigVar_3, [['reapTime', '180'], ['connectionTimeout', '180'], ['minConnections', '1'], ['unusedTimeout', '1800'], ['agedTimeout', '0'], ['purgePolicy', 'EntirePool'], ['maxConnections', '10']])

print 'Starting Creating Variables'
AdminTask.setVariable(['-scope', 'Node=' + NodeName, '-variableName', 'DERBY_JDBC_DRIVER_PATH', '-variableValue', '${WAS_INSTALL_ROOT}/derby/lib'])

print 'Starting Saving Configuration Changes Before Application Deployment'
AdminConfig.save()
print 'Starting Application Deployment'
AdminConfig.create('Library', Server, [['name', 'globalSharedLibrary'], ['classPath',  '/work/config/lib']])
appServer = AdminConfig.list('ApplicationServer',Server)
classLoader1 = AdminConfig.create('Classloader', appServer, [['mode',  'PARENT_FIRST']])
AdminConfig.create('LibraryRef', classLoader1, [['libraryName', 'globalSharedLibrary']])
#AdminApp.install('/path/to/defaultapplication.war', ["-node", NodeName, "-server", "server1", "-appname", "defaultapplication.war", "-CtxRootForWebMod", [["Default Web Application", "javax-servlets-1.0-SNAPSHOT.war,WEB-INF/web.xml", "/"]]])
AdminConfig.save()

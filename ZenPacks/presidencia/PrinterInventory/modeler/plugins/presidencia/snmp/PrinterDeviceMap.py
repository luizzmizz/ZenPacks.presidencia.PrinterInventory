from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap
from Products.DataCollector.plugins.DataMaps import ObjectMap,MultiArgs
from Products.DataCollector.EnterpriseOIDs import EnterpriseOIDs
import logging
import re

logger = logging.getLogger('zen.ZenModeler')

class PrinterDeviceMap(SnmpPlugin):
    maptype = "PrinterDeviceMap"
    snmpGetMap = GetMap({ 
             '.1.3.6.1.2.1.43.5.1.1.17.1': 'setHWSerialNumber',
             '.1.3.6.1.2.1.25.3.2.1.3.1': 'modelName',
             '.1.3.6.1.2.1.1.2.0' : 'snmpOid',
             })

    def process(self, device, results, log):
        getData, tabledata = results
        om = self.objectMap()
        if not getData.has_key('setHWSerialNumber') or not getData['setHWSerialNumber']:
          om.setHWSerialNumber='N/A'
        else:
          om.setHWSerialNumber=getData['setHWSerialNumber']

        if getData['snmpOid']:
            match = re.match(r'(.\d+){7}',getData['snmpOid'])
            if match:
                manufacturer = EnterpriseOIDs.get(match.group(0), None)
            else:
                manufacturer = None
            if getData.has_key('modelName'):
              om.setHWProductKey = MultiArgs(getData['modelName'], manufacturer)
            else:
              om.setHWProductKey = MultiArgs(getData['snmpOid'], manufacturer)
            log.debug("HWProductKey=%s", om.setHWProductKey)
        return om



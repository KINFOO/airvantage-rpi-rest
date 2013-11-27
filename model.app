<?xml version="1.0" encoding="ISO-8859-1"?>
<app:application xmlns:app="http://www.sierrawireless.com/airvantage/application/1.0" 
        type="com.test.airvantagepiapp" 
        name="AirVantage Pi App"
        revision="0.0.1">
 <capabilities>

  <communication>
   <protocol comm-id="SERIAL" type="REST" />
  </communication>

  <data>
   <encoding type="REST">
    <asset default-label="AirVantage Pi" id="airvantagepi">
     <variable default-label="Temperature" path="temperature" type="double"/>
      <setting default-label="Threshold" path="threshold" type="int"/>
     </asset>
   </encoding>
  </data>

 </capabilities>
</app:application>

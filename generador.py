state=0
offset=0
f=open("P18F45K80.INC","r")
archivo=f.read()
f.close()
f=open("config.xml","w")
for line in archivo.split("\n"):
    #if state==0:
    if ";----- CONFIG" in line:
        if offset>0:
            f.write('  </config>\r\n\r\n')
        tmp=line.split(" ")
        nameConfig=tmp[1]
        #print(nameConfig)
        f.write('  <config offset="0x{:X}" name="{:s}" wmask="0xFF" bvalue="0xZZ" >\r\n'.format(offset,nameConfig))
        offset+=1
        #state=1
        tmp2=[]
        #dic={}
        #state=1
    if ";----- DEVID" in line:
        f.write('  </config>\r\n\r\n')
        break
    if offset>0:
        if line == "":
            try:
                #state=0
                print(tmp2)
                f.write('    <mask name="{:s}"  value="0xZZ" >\r\n'.format(tmp2[0]["name"]))
                mask=0xff
                #print(tmp2)
                for datos in tmp2:
                    mask=mask&int(datos["value"],16)
                for datos in tmp2:
                    #print(datos)
                    tmp=datos["name"]+'_'+datos["name2"]+'"'
                    f.write('      <value value="0x{0:02X}" name="{2:<14}def="_{1:<16}/>\r\n'.format(int(datos["value"],16)^mask,tmp,datos["name2"]+'"'))
                tmp2=[]
                f.write('    </mask>\r\n')
                #f.write('    </mask>\r\n')
            #break
            #print(mask)
            except:
                pass
            
        #if
        #try:
        elif line[0]=="_":
            tmp=line.split()
            #print(tmp)
            #dic["name"]=tmp[0].split("_")[1]
            #dic["name2"]=tmp[0].split("_")[2]
            #dic["value"]=tmp[2].split("'")[1]
            tmp2.append({"name":tmp[0].split("_")[1],"name2":tmp[0].split("_")[2],"value":tmp[2].split("'")[1]})
            #print(tmp[11].split("'"))
            #print(dic)
            #print(tmp2)
            #tmp2.append(dic)
            #print(tmp2)
            #print("blacon")
        #except:
            #pass
f.close()
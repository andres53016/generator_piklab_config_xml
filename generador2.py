state=0
offset=0
config={"300000":"CONFIG1L","300001":"CONFIG1H","300002":"CONFIG2L","300003":"CONFIG2H","300005":"CONFIG3H","300006":"CONFIG4L","300008":"CONFIG5L","300009":"CONFIG5H","30000A":"CONFIG6L","30000B":"CONFIG6H","30000C":"CONFIG7L","30000D":"CONFIG7H"}
f=open("part_of_8bit_device.info","r")
archivo=f.read()
f.close()
f=open("config.xml","w")
for line in archivo.split("\n"):
    #if state==0:
    tmp=line.replace("<","").split(">")
    #print(tmp)
    try:
        tmp.remove("")
    except:
        pass
    if tmp[0]=="CONFIGREG_INFO_TYPE":
        if offset>0:
            f.write('    </mask>\r\n')
            f.write('  </config>\r\n\r\n')
        #tmp=line.split(" ")
        nameConfig=tmp[1]
        kk=0
        #print(nameConfig)
        f.write('  <config offset="0x{:X}" name="{:s}" wmask="0xFF" bvalue="0x{:02X}" >\r\n'.format(offset,config[tmp[1].upper()],int(tmp[3],16)))
        offset+=1
        otro=0
        #state=1
        #tmp2=[]
        #dic={}
        #state=1
    elif tmp[0]=="SWITCH_INFO_TYPE":
        if otro>0:
            f.write('    </mask>\r\n')
        f.write('    <mask name="{:s}"  value="0x{:02X}" >\r\n'.format(tmp[1],int(tmp[3],16)))
        name=tmp[1]
        otro+=1
        #kk|=int(tmp[3],16)
        #print(hex(kk))
    elif tmp[0]=="SETTING_VALUE_TYPE":
        tmp2=name+"_"+tmp[1]+'"'
        f.write('      <value value="0x{0:02X}" name="{1:<14}def="_{2:<16}/>\r\n'.format(int(tmp[3],16),tmp[1]+'"',tmp2))
    #if ";----- DEVID" in line:
        #f.write('  </config>\r\n\r\n')
        #break
    #if offset>0:
        #if line == "":
            #try:
                ##state=0
                #print(tmp2)
                #f.write('    <mask name="{:s}"  value="0xZZ" >\r\n'.format(tmp2[0]["name"]))
                #mask=0xff
                ##print(tmp2)
                #for datos in tmp2:
                    #mask=mask&int(datos["value"],16)
                #for datos in tmp2:
                    ##print(datos)
                    #tmp=datos["name"]+'_'+datos["name2"]+'"'
                    #f.write('      <value value="0x{0:02X}" name="{2:<14}def="_{1:<16}/>\r\n'.format(int(datos["value"],16)^mask,tmp,datos["name2"]+'"'))
                #tmp2=[]
                #f.write('    </mask>\r\n')
                #f.write('    </mask>\r\n')
            #break
            #print(mask)
            #except:
                #pass
            
        #if
        #try:
        #elif line[0]=="_":
            #tmp=line.split()
            #print(tmp)
            #dic["name"]=tmp[0].split("_")[1]
            #dic["name2"]=tmp[0].split("_")[2]
            #dic["value"]=tmp[2].split("'")[1]
            #tmp2.append({"name":tmp[0].split("_")[1],"name2":tmp[0].split("_")[2],"value":tmp[2].split("'")[1]})
            #print(tmp[11].split("'"))
            #print(dic)
            #print(tmp2)
            #tmp2.append(dic)
            #print(tmp2)
            #print("blacon")
        #except:
            #pass
f.write('    </mask>\r\n')
f.write('  </config>\r\n\r\n')
f.close()
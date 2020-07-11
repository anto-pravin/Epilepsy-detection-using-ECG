from os import path
for i in range(1,420):
    for j in [1,2,3]:
        try:
            txt_file = str(i)+'_'+str(j)+'.txt'
            file_txt = open(txt_file)
            directory = 'C:/Users/Anto Pravin/Desktop/sample/csv'
            file_name = str(i)+'_'+str(j)+'.csv'
            file_path = path.join(directory,file_name)
            file = open(file_path,'w')
            file.write(str(i)+'_'+str(j)+'\n')
            for lines in file_txt:
                l = lines.split('\t')
                file.write('\n'.join(l))
            file.close()
            file_txt.close()
        except:
            pass
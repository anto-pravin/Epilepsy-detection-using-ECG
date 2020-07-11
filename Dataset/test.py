from os import path
txt_file = str(2)+'_'+str(1)+'.txt'
file_txt = open(txt_file)
directory = 'C:/Users/Anto Pravin/Desktop/sample/csv'
file_name = str(2)+'_'+str(1)+'.csv'
file_path = path.join(directory,file_name)
file = open(file_path,'w')
file.write(str(2)+'_'+str(1)+'\n')
for lines in file_txt:
    l = lines.split('\t')
    file.write('\n'.join(l))
file.close()
file_txt.close()
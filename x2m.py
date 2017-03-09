import reader,sys
print '[*] MySQL configs'
host = raw_input('         host      : ')
username = raw_input('         username  : ')
password = raw_input('         password  : ')
database = raw_input('         database  : ')
fil = raw_input('         Exel file : ')
print '[*] setup settings to buil the php script'
print '        Tables exists on the file:',
tables = reader.infoxlsx(fil)
print ' , '.join(tables)

table = raw_input('        table name       : ')
def unilong(x):
    typ = type(x)
    if typ.__name__ == 'long':
        x= str(x)
    elif typ.__name__ == 'unicode':
        x = x.encode('utf8')
    return x
def rms(x):
    x = unilong(x)
    x = x.replace('-','')
    x = x.replace('\'','')
    x = x.replace('/','')
    x = x.replace('%','')
    x = x.replace('!','')
    x = x.replace('?','')
    x = x.replace('*','')
    x = x.replace('+','')
    x = x.replace('.','')
    x = x.replace('"','')
    x = x.replace('=','')
    x = x.replace(' ','')
    return x
tab = rms(table)
output = raw_input('        output file name : ')
prompt = raw_input('[?] are you sure you want to continue (answer with "yes" or "no"):')
if prompt=="yes":
    pass
else:
    print 'bye'
    sys.exit()
lista = reader.Readxlsx(fil,table)
if len(lista)==0:
    print 'Table',table,'is empty.'
    sys.exit()
else:
    pass
f = open(output,'w+')
f.writelines( '<?php\n\n$host = "'+host+'";\n$username = "'+username+'";\n$password = "'+password+'";\n$database = "'+database+'";\n\n// Create connection\n\n$conn = new mysqli($host, $username, $password,$database);\n\n// Check connection\n\nif ($conn->connect_error) {\n\n    die("Connection failed: " . $conn->connect_error);\n\n}')
f.writelines('\nset_time_limit(200);\n')
f.writelines('\n$sqltabel = "CREATE TABLE '+tab+'(\
\n      id MEDIUMINT NOT NULL AUTO_INCREMENT,\n')
j=0
for i in lista[0]:
    j=j+1
    if i==None:
        sj = 'None'+str(j)
        f.writelines( '      '+sj+' TEXT NOT NULL,\n')
    else:
        f.writelines( '      '+str(i)+' TEXT NOT NULL,\n')

f.writelines( '     PRIMARY KEY (id));";\n')
f.writelines( 'if ($conn->query($sqltabel) === TRUE) { echo "Table '+tab+' created.\n";} else {echo "Table not created: " . $conn->error."</br>";}')
headers = list()
j=0
for i in lista[0]:
    if i == None:
        j=j+1
        h='None'+str(j)
        headers.append(h)
        h=''
    else:
        headers.append(i)

com = '$sql = \'insert into '+tab+' ('+','.join(headers)+') values('
j = 0
f.writelines( '\n')
for i in lista:
    if j==0:
        j=j+1
        pass
    else:
        j = j+1
        f.writelines(com)
        m = 0
        for k in i:
            if m==len(i)-1:
                if k ==None:
                    f.writelines('"None"')
                else:
                    k=unilong(k)
                    k = (str(k)).replace("'","\\'")
                    k = (str(k)).replace('"','\\"')
                    f.writelines('"'+str(k)+'"')
            else:
                m = m+1
                if k ==None:
                    f.writelines('"None",')
                else:
                    k = unilong(k)
                    k = (str(k)).replace("'","\\'")
                    k = (str(k)).replace('"','\\"')
                    f.writelines('"'+str(k)+'",')
        f.writelines(')\';\n')
        f.writelines( 'if ($conn->query($sql) === TRUE) { echo "data inserted.</br>"; } else {echo "Data not inserted: " . $conn->error."</br>";}\n')
f.writelines('$conn->close();')
f.writelines('\n?>')
f.close()
print '[*] php file: '+output+' builded'
prompt = raw_input('[!] do you want a file to display your data(answer "yes" or "no"):')
if prompt == 'yes':
    pass
else:
    print '[*] Script by Abd-Elilah.'
    sys.exit()
print '[*] display file name :',
dfile = raw_input('')
nf = open(dfile,'w+')
nf.writelines( '<?php\n\n$host = "'+host+'";\n$username = "'+username+'";\n$password = "'+password+'";\n$database = "'+database+'";\n\n// Create connection\n\n$conn = new mysqli($host, $username, $password,$database);\n\n// Check connection\n\nif ($conn->connect_error) {\n\n    die("Connection failed: " . $conn->connect_error);\n\n}')
nf.writelines('\nset_time_limit(200);\n')
nf.writelines('$sql = \'select id,'+','.join(headers)+' from '+tab+'\';\n')
nf.writelines('echo "<style>\ntr:hover {\nbackground: #DBECF9;\n}\ntr:active {\nbackground: #9DCCEE;\n}\ntr {\nbackground: ;\n}\n</style>";')
display = 'echo "<table border=\'1\'  width=\'100%\' cellspacing=\'0\' cellpadding=\'0\' bordercolorlight=\'#993333\' bordercolordark=\'#FF0000\'>\n<tr>'
nf.writelines(display)
for i in headers:
    display = '<td>'+str(i)+'</td>'
    nf.writelines(display)
nf.writelines('</tr>";\n')
nf.writelines('$result = $conn->query($sql);\n')
nf.writelines( 'if ($result->num_rows > 0) {\n// output data of each row\nwhile($row = $result->fetch_assoc()) {\n')
nf.writelines('echo "<tr>')
for i in headers:
    display = '<td>".$row["'+str(i)+'"]."</td>'
    nf.writelines(display)
    nf.writelines('\n   ')
nf.writelines('</tr>";\n')
nf.writelines('    }\n} else {\n    echo "0 results";}\n')
nf.writelines('echo "</table>";\n')
nf.writelines('$conn->close();')
nf.close()

print '[*] Script By Abd Elilah.'


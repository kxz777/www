import sys
sys.path.append('/home/centos/www/Bibliotecas/Dizu')
import ConectarDizu
import LoginDizu

username  = 'vilellagds@gmail.com'
password  = 'Werq9137di'
cookies   = login(username, password)
accountId = getAccountId('spontaneousdrawing4fun', cookies)
task      = getTask(accountId, cookies)
print (task)
print ('\n')
resp      = input ('Fez a tarefa?\n')
confirmed = confirmTask(accountId, task, cookies) 
print (confirmed)
import win32serviceutil
import win32service
import win32event
import servicemanager
import time
import subprocess
import sys
import os

class MeuServico(win32serviceutil.ServiceFramework):
    _svc_name_ = "EmailServicePythonExcel"
    _svc_display_name_ = "serviço de Envio de Email de Cobrança Python"
    _svc_description_ = "Serviço que executa um script Python uma vez por dia"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.running = True

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        self.running = False
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))

        self.main()

    def main(self):
        # Definir o horário de execução (24h)
        hora_execucao = 19  # 19 horas (2 PM)

        while self.running:
            agora = time.localtime()
            if agora.tm_hour == hora_execucao and agora.tm_min == 0:
                # Caminho completo para o seu script
                caminho_script = r"D:\Projetos\PYPROJECTS\pyEmailExcel\app.py"
                
                # Executar o script
                subprocess.call([sys.executable, caminho_script])
                
                # Aguardar um minuto para evitar execuções múltiplas no mesmo minuto
                time.sleep(60)
            else:
                # Aguardar um minuto antes de verificar novamente
                time.sleep(60)

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(MeuServico)

import subprocess


class command:
    def run(self, shell): subprocess.run(args=shell, shell=True, check=True)

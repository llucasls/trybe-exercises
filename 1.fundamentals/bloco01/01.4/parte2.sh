#!/usr/bin/env sh

# Navegue até a pasta `unix_tests`;
cd ../01.3/unix_tests

# Rode o comando `[ls](https://linux.die.net/man/1/ls) -l` e veja quais as
# permissões dos arquivos;
ls -l

# Mude a permissão do arquivo `bunch_of_things.txt` para que todos os usuários
# possam ter acesso à leitura e escrita, e verifique se está correto com o
# comando `ls -l`;
chmod a=rw bunch_of_things.txt
# chmod 666 bunch_of_things.txt
ls -l

# Tire a permissão de escrita do arquivo `bunch_of_things.txt` para todos os
# usuários. Verifique se está correto com o comando `ls -l`;
chmod a-w bunch_of_things.txt
ls -l

# Volte a permissão do arquivo `bunch_of_things.txt` para a listada inicialmente
# utilizando o comando `chmod 644 bunch_of_things.txt`.
chmod 644 bunch_of_things.txt
ls -l

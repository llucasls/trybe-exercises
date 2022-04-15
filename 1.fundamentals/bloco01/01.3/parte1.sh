#!/usr/bin/env sh

# Exercícios 1 a 13

# Utilizando o terminal, aplique o comando de criação de diretórios que você
# aprendeu, crie um diretório chamado `unix_tests` e navegue até ele.
mkdir unix_tests
cd unix_tests

# Crie um arquivo de texto com o nome `trybe.txt`.
touch trybe.txt

# Crie uma cópia do arquivo `trybe.txt` com nome `trybe_backup.txt`.
cp trybe.txt trybe_backup.txt

# Renomeie o arquivo `trybe.txt`.
mv trybe.txt xablau.txt

# Dentro de `unix_tests`, crie um novo diretório chamado `backup`.
if test $(basename $PWD) = 'unix_tests'; then
  mkdir backup
fi

# Mova o arquivo `trybe_backup.txt` para o diretório `backup`.
mv trybe_backup.txt backup/

# Dentro de `unix_tests`, crie um novo diretório chamado `backup2`.
if test $(basename $PWD) = 'unix_tests'; then
  mkdir backup2
fi

# Mova o arquivo `trybe_backup.txt` da pasta `backup` para a pasta `backup2`.
mv backup/trybe_backup.txt backup2/

# Apague a pasta `backup`.
rmdir backup

# Renomeie a pasta `backup2` para `backup`.
mv backup2 backup

# Veja qual o path completo do diretório atual e liste todos os arquivos dentro dele.
pwd
ls

# Apague o diretório `backup`.
rm -rf backup

# Limpe o terminal.
clear

# Volte ao diretório anterior
cd ..

# Exercícios 14 a 16

# Mostre na tela as 5 primeiras skills do arquivo `skills.txt`.
head -n 5 skills.txt
# cat skills.txt | head -n 5

# Mostre na tela as 4 últimas skills do arquivo `skills.txt`.
tail -n 4 skills.txt
# cat skills.txt | tail -n 4

# Apague todos os arquivos que terminem em `.txt` .
rm *.txt

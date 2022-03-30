ansible-galaxy install -r requirements.yml

ansible-playbook main.yaml -i environments/dev-simple/inventory.yaml -t common -l app2

sudo psql -h 192.168.56.21 -p 5432 -d app -U worker

ansible-vault encrypt_string 'worker' --vault-id=app@.vault/app.key

pg_basebackup --host=192.168.56.21 --pgdata=/var/lib/postgresql/12/main -R -U postgres


pg_basebackup --host=192.168.56.21 --username=repluser --pgdata=/var/lib/postgresql/10/main --wal-method=stream --write-recovery-conf

sudo -u postgres psql postgres # разблокировать учетную запись postgres в ubuntu
-------------
sudo -u postgres -i

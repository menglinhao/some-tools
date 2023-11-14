import os

fabric_mlh = "\nalias fabric_mlh='/root/mlh/operation/venv/bin/python /root/mlh/operation/script/fabric_deploy.py'"
fabric_deploy = "\nalias fabric_deploy='/home/pyweb/nslb_operation/operation/venv/bin/python /home/pyweb/nslb_operation/operation/script/fabric_deploy.py'"
slb_error_tail = '\nalias slb_error_tail="tail -f -n1000 /var/log/normae/slb_error.log"'
slb_access_tail = '\nalias slb_access_tail="tail -f -n1000 /var/log/normae/slb_access.log"'
lbagent_tail = '\nalias lbagent_tail="tail -f -n1000 /var/log/normae/lbagent.log"'
docker_rmi_none = '''\nalias docker_rmi_none='docker rmi $(docker images -f "dangling=true" -q)' '''
health_check_tail = (
    '\nalias health_check_tail="tail -f -n1000 /var/log/normae/health_check/health_check.log"'
)
controller_tail = (
    '\nalias controller_tail="tail -f -n1000 /var/log/normae/controller/controller.log"'
)
gin_tail = '\nalias gin_tail="tail -f -n1000 /var/log/normae/controller/gin.log"'
gorm_tail = '\nalias gorm_tail="tail -f -n1000 /var/log/normae/controller/gorm.log"'
license_tail = '\nalias license_tail="tail -f -n1000 /var/log/normae/license_store.log"'
help_test_tail = '\nalias help_test_tail="tail -f -n1000 /var/log/normae/help_test/django.log"'
help_test_ngx_acc_tail = '\nalias help_test_ngx_acc_tail="tail -f -n1000 /var/log/normae/help_test/ngx_acc.log"'
help_test_ngx_err_tail = '\nalias help_test_ngx_err_tail="tail -f -n1000 /var/log/normae/help_test/ngx_err.log"'


vim_controller_conf = (
    '\nalias vim_controller_conf="vim /etc/normae/go-controller/config/config.json"'
)
vim_nginx_conf = (
    '\nalias vim_nginx_conf="vim /etc/normae/nginx/nginx.conf"'
)
vim_normae_compose_yml = (
    '\nalias vim_normae_compose_yml="vim /opt/normae/images/docker-compose.yml"'
)
vim_resty_json = (  # qmti
    '\nalias vim_resty_json="cat /var/normae/nginx/resty_conf.json | python3 -m json.tool > /tmp/resty_conf.json && vim /tmp/resty_conf.json"'
)  # %!python3 -m "json.tool"
vim_hc_server_node = ( 
    '\nalias vim_hc_server_node="cat /var/normae/nginx/server_node.json | python3 -m json.tool > /tmp/server_node.json && vim /tmp/server_node.json"'
)  # %!python3 -m "json.tool"
vim_lbagent_conf = ( 
    '\nalias vim_lbagent_conf="vim /etc/normae/lbagent/config.yml"'
)


write_content_list = [
    fabric_mlh, fabric_deploy, slb_error_tail, slb_access_tail, lbagent_tail,
    docker_rmi_none, health_check_tail, controller_tail, gin_tail, gorm_tail,
    vim_nginx_conf, vim_controller_conf, vim_normae_compose_yml, 
    vim_resty_json, vim_hc_server_node, vim_lbagent_conf, license_tail,
    help_test_tail,
    help_test_ngx_acc_tail,
    help_test_ngx_err_tail,
]

files = ("/root/.bashrc", "/root/.zshrc")
for file in files:
    if not os.path.exists(file):
        continue
    with open(file, mode="+a") as f:
        for content in write_content_list:
            f.write(content)

os.system("source /root/.bashrc")

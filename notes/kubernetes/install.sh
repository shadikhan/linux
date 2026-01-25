(.venv) shad@linux:~$ curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-linux-amd64
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100  133M  100  133M    0     0   187M      0 --:--:-- --:--:-- --:--:--  187M
(.venv) shad@linux:~$ sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64
(.venv) shad@linux:~$ curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   138  100   138    0     0   2075      0 --:--:-- --:--:-- --:--:--  2090
100 55.8M  100 55.8M    0     0   168M      0 --:--:-- --:--:-- --:--:--  168M
(.venv) shad@linux:~$ sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
(.venv) shad@linux:~$ kubectl version --client
Client Version: v1.35.0
Kustomize Version: v5.7.1

(.venv) shad@linux:~$ minikube start
😄  minikube v1.37.0 on Ubuntu 24.04
👎  Unable to pick a default driver. Here is what was considered, in preference order:
💡  Alternatively you could install one of these drivers:
    ▪ docker: Not installed: exec: "docker": executable file not found in $PATH
    ▪ kvm2: Not installed: exec: "virsh": executable file not found in $PATH
    ▪ podman: Not installed: exec: "podman": executable file not found in $PATH
    ▪ qemu2: Not installed: exec: "qemu-system-x86_64": executable file not found in $PATH
    ▪ virtualbox: Not installed: unable to find VBoxManage in $PATH

❌  Exiting due to DRV_NOT_DETECTED: No possible driver was detected. Try specifying --driver, or see https://minikube.sigs.k8s.io/docs/start/

(.venv) shad@linux:~$ sudo apt update

(.venv) shad@linux:~$ sudo apt install -y qemu-kvm libvirt-daemon-system libvirt-clients virtinst

(.venv) shad@linux:~$ sudo usermod -aG libvirt $USER
(.venv) shad@linux:~$ sudo usermod -aG kvm $USER
(.venv) shad@linux:~$ newgrp libvirt
(.venv) shad@linux:~$ minikube start --driver=kvm2
😄  minikube v1.37.0 on Ubuntu 24.04
✨  Using the kvm2 driver based on user configuration
💾  Downloading driver docker-machine-driver-kvm2:
    > docker-machine-driver-kvm2-...:  65 B / 65 B [---------] 100.00% ? p/s 0s
    > docker-machine-driver-kvm2-...:  15.20 MiB / 15.20 MiB [ 100.00% ? p/s 0s
💿  Downloading VM boot image ...
    > minikube-v1.37.0-amd64.iso....:  65 B / 65 B [---------] 100.00% ? p/s 0s
    > minikube-v1.37.0-amd64.iso:  370.78 MiB / 370.78 MiB  100.00% 316.32 MiB 
👍  Starting "minikube" primary control-plane node in "minikube" cluster
💾  Downloading Kubernetes v1.34.0 preload ...
    > preloaded-images-k8s-v18-v1...:  337.07 MiB / 337.07 MiB  100.00% 198.77 
🔥  Creating kvm2 VM (CPUs=2, Memory=3072MB, Disk=20000MB) ...
🐳  Preparing Kubernetes v1.34.0 on Docker 28.4.0 ...
🔗  Configuring bridge CNI (Container Networking Interface) ...
🔎  Verifying Kubernetes components...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🌟  Enabled addons: default-storageclass, storage-provisioner
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default

(.venv) shad@linux:~$ kubectl get nodes
NAME       STATUS   ROLES           AGE     VERSION
minikube   Ready    control-plane   5m15s   v1.34.0
(.venv) shad@linux:~$ kubectl get pods -A
NAMESPACE     NAME                               READY   STATUS    RESTARTS        AGE
kube-system   coredns-66bc5c9577-kn6lq           1/1     Running   0               5m10s
kube-system   etcd-minikube                      1/1     Running   0               5m16s
kube-system   kube-apiserver-minikube            1/1     Running   0               5m16s
kube-system   kube-controller-manager-minikube   1/1     Running   0               5m16s
kube-system   kube-proxy-5h6t4                   1/1     Running   0               5m11s
kube-system   kube-scheduler-minikube            1/1     Running   0               5m16s
kube-system   storage-provisioner                1/1     Running   1 (4m40s ago)   5m14s
```




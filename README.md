# ʹ���ٻ�����ע����������޸Ĺ���

? **��������**  
�����߽���ѧϰ����ʹ�ã��Ͻ�������ҵ��;���޸�ע�����ڷ��գ�����ǰ�����б������ݡ���ʹ�ñ�������ɵ��κ���ʧ�����߸Ų�����

---

## ? ����˵��

- �Զ��޸ġ�ʹ���ٻ����Ρ���Windowsע����е���������ز���
- ֧�ֶ�̬ƥ�������Ϸģʽ(PVE/PVP/TD/Br��)���Զ���������
- �޸ļ�ֵ���ֽ�Ϊ `0x01`�������������߼�(����Ч������Ϸ�汾���ܲ�ͬ)

---

## ? ������ʹ��

### ��ʽһ��ֱ������EXE���Ƽ���

1. ǰ�� [Releaseҳ��](https://github.com/DreamChaserWhatever/regedit_CallofDuty/releases) �������°汾
2. **�Ҽ��Թ���Ա�������**(����ϵͳȨ��)
3. ����ʾ��ɲ�����������Զ��޸�ע���

### ��ʽ������Դ�����У�Python 3.13��

1. ��¡�ֿ⣺
    ```bash
    git clone https://github.com/DreamChaserWhatever/regedit_CallofDuty.git
2. ��װ�����⣺
   ```bash
   pip install -r requirements.txt
3. ����������
    ```bash
   python main.py

---

## ? EXE���ָ��

### �������

1. ȷ���Ѱ�װȫ��������
   ```bash
   pip install -r requirements.txt
2. ִ�д������(����ǰ׼��app.icoͼ�� �� ʹ���Դ���main.ico)��
   ```bash
   pyinstaller --onefile --icon=main.ico main.py -n "CODM_Sensitivity_Tool"
3. ���ɵ�exe�ļ�λ��distĿ¼

---

## ?? ����ϸ��

- **ע���·��**��`HKEY_CURRENT_USER\SOFTWARE\Tencent\Call-of-Duty`
- **ƥ�����**��ʹ��������ʽɸѡĿ���ֵ��
  ```regex
  ^CODM_\d+_iMSDK_CN_(PVE|PVP|TD|Br|PVEFiring|PVPFiring|TDFiring|BrFiring)(_(?:RotateSensitive|AimRotate|ReddotHolo|Sniper|Free|ACOG|[\dX]+|SkyVehicle|GroundVehicle|Vertical|Ult).*?)?_h\d+$

---

## ?? ע������

1. **����ʹ�ù���ԱȨ������**�������޷��޸�ע���
2. ��Ϸ���º���ܵ�������ʧЧ�����������й���
3. ��ȫ��������飺
    - ��ʱ�ر�ʵʱ����
    - ��exe�ļ���ӵ�������
4. �״�ʹ�ý���ͨ��ע���༭���������·����
   ```reg
   HKEY_CURRENT_USER\SOFTWARE\Tencent\Call-of-Duty

---

? **��Ҫ˵��**  
�������к�����ʾ`[�޸����޸����]`����ʾ���з���������ע����ֵ�Ѵ�����ɡ�����������Ϸ��ʹ�޸���Ч��
---

## ? ��ԴЭ��

����Ŀ���� **[MIT License](LICENSE)** ��Դ��������������Ȩ����

- ? **����ʹ��**�������������ڸ���/ѧϰ��;
- ? **���ο���**�������޸�Դ���벢���������汾
- ? **����ַ�**�������ɷ���Դ�������ĳ���

**ΨһԼ��**��  
? ���ηַ�ʱ�������ԭʼ���֤�ļ���������������Դ���ļ�ͷ��ע�ͣ�

---

## ? ֧���빱��

### ���ⷴ���뽨��

[![GitHub Issues](https://img.shields.io/github/issues/DreamChaserWhatever/regedit_CallofDuty?color=blue)](https://github.com/DreamChaserWhatever/regedit_CallofDuty/issues)

1. ����BUG?���ύ [Issue](https://github.com/DreamChaserWhatever/regedit_CallofDuty/issues) ���ṩ��
    - �����ͼ/��־
    - ����ϵͳ�汾
    - ��Ϸ�ͻ��˰汾

### ���빱��

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/DreamChaserWhatever/regedit_CallofDuty/pulls)

1. Fork ���ֿⲢ�����·�֧
2. �ύ���������븽������˵����
3. ���� Pull Request �� `dev` ��֧

### ��������ϵ

- ? **Bilibili**��[һ��ǽ��˫��](https://space.bilibili.com/3546759762545419)����λ�����ҵ��ģ�
- ? **Bilibili**��[DC���](https://space.bilibili.com/3493117248407780)����ֻ��д�������λ��
- ? **GitHub**��[DreamChaserWhatever](https://github.com/DreamChaserWhatever)

> �������Ŀ�����а������������Ͻ� ? **Star** ֧�ֿ����߳������£�
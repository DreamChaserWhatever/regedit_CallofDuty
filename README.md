# ʹ���ٻ�����ע����������޸Ĺ���

:warning: **��������**  
�����߽���ѧϰ����ʹ�ã��Ͻ�������ҵ��;���޸�ע�����ڷ��գ�����ǰ�����б������ݡ���ʹ�ñ�������ɵ��κ���ʧ�����߸Ų�����

---

## :gear: ����˵��

- �Զ��޸ġ�ʹ���ٻ�ģ�������Ρ���Windowsע����е���������ز���
- ֧�ֶ�̬ƥ�������Ϸģʽ��PVE/PVP/TD/Br�ȣ����Զ���������
- �޸ļ�ֵ���ֽ�Ϊ `0x01`�������������߼�������Ч������Ϸ�汾���ܲ�ͬ��

---

## :rocket: ������ʹ��

### ��ʽһ��ֱ������EXE���Ƽ���

1. ǰ�� [Releaseҳ��](https://github.com/DreamChaserWhatever/regedit_CallofDuty/releases) �������°汾
2. ʹ��ǰӦ����Ϸ���ÿһ�������ȶ��϶�һ��,��ֹ��һЩû�иĵ�(ֻ�ж��������òŻ�����ע���)
3. **�Ҽ��Թ���Ա�������**������ϵͳȨ�ޣ�
4. ����ʾ��ɲ�����������Զ��޸�ע���

### ��ʽ������Դ�����У�Python 3.13��

1. ��¡�ֿ⣺
    ```bash
    git clone https://github.com/DreamChaserWhatever/regedit_CallofDuty.git
    ```
2. ��װ�����⣺
    ```bash
    pip install -r requirements.txt
    ```
3. ����������
    ```bash
    python main.py
    ```

---

## :package: EXE���ָ��

### �������

1. ȷ���Ѱ�װȫ��������
    ```bash
    pip install -r requirements.txt
    ```
2. ִ�д���������ǰ׼�� `app.ico` ͼ�� �� ʹ���Դ��� `main.ico`����
    ```bash
    pyinstaller --onefile --icon=main.ico main.py -n "CODM_Sensitivity_Tool"
    ```
3. ���ɵ�exe�ļ�λ�� `dist` Ŀ¼

---

## :mag: ����ϸ��

- **ע���·��**��`HKEY_CURRENT_USER\SOFTWARE\Tencent\Call-of-Duty`
- **ƥ�����**��ʹ��������ʽɸѡĿ���ֵ��
  ```regex
  ^CODM_\d+_iMSDK_CN_(PVE|PVP|TD|Br|PVEFiring|PVPFiring|TDFiring|BrFiring)(_(?:RotateSensitive|AimRotate|ReddotHolo|Sniper|Free|ACOG|[\dX]+|SkyVehicle|GroundVehicle|Vertical|Ult).*?)?_h\d+$
---

## :warning: ע������

1. **����ʹ�ù���ԱȨ������**�������޷��޸�ע���
2. ��Ϸ���º���ܵ�������ʧЧ�����������й���
3. ��ȫ��������飺
    - ��ʱ�ر�ʵʱ����
    - ��exe�ļ���ӵ�������
4. �״�ʹ�ý���ͨ��ע���༭���������·����
   ```reg
   HKEY_CURRENT_USER\SOFTWARE\Tencent\Call-of-Duty

---

:information_source: **��Ҫ˵��**  
�������к�����ʾ`[�޸����޸����]`����ʾ���з���������ע����ֵ�Ѵ�����ɡ�����������Ϸ��ʹ�޸���Ч��
---

## :book: ��ԴЭ��

����Ŀ���� **[MIT License](LICENSE)** ��Դ��������������Ȩ����

- :white_check_mark: **����ʹ��**�������������ڸ���/ѧϰ��;
- :white_check_mark: **���ο���**�������޸�Դ���벢���������汾
- :white_check_mark: **����ַ�**�������ɷ���Դ�������ĳ���

**ΨһԼ��**��  
:information_source: ���ηַ�ʱ�������ԭʼ���֤�ļ���������������Դ���ļ�ͷ��ע�ͣ�

---

## :sparkles: ֧���빱��

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

- :tv: **Bilibili**��[һ��ǽ��˫��](https://space.bilibili.com/3546759762545419)����λ�����ҵ��ģ�
- :tv: **Bilibili**��[DC���](https://space.bilibili.com/3493117248407780)����ֻ��д�������λ��
- :octocat: **GitHub**��[DreamChaserWhatever](https://github.com/DreamChaserWhatever)

> �������Ŀ�����а������������Ͻ� :sparkles: **Star** ֧�ֿ����߳������£�
a
    �i�_�-  �                   @   s"   d dl T dd� Zdd� Ze�  dS )�    )�*c                  C   s�   t t� � t�  t�d� t�  ttd t �} ttd t �}d}d}| |krz||krzt	�
d� t td � t	�
d� nt td	 � t�  d S )
Nzcat banner/login_banner.txtz	USERNAME:z	PASSWORD:Z7AZABETz	El Korsang      �?z[+] Done Successfully ^__^ �   z[!] NOT FOUND)�print�R�clear�os�system�space�input�W�y�time�sleep�G�exit)�USERNAMEZPASSWORD�user�passwd� r   �5/root/Desktop/7azabet/decrypt_hash_tool/final_baqa.py�login   s    


r   c                  C   s  dd l } dd l}t�  t�  tdt� d�� | �d� tdt �}ttd t �}|dkr`d}n|}| �d	� �z^t	|d
d���:}|D �]}|�
� }t|�dkr�|�|�� ��� }||kr�td|� d�� | �d�  �q��n�t|�t|�d�� ��� �k�rH|�|�� ��� }d}||k�rdtd|� d|� d�� | �d�  �q��nt|�t|�d�� ��� �k�r�|�|�� ��� }d}||k�rdtd|� d|� d�� | �d�  �q��n�t|�t|�d�� ��� �k�r|�|�� ��� }d}||k�rdtd|� d|� d�� | �d�  �q��nHt|�t|�d�� ��� �k�r�|�|�� ��� }d}||k�rdtd|� d|� d�� | �d�  �q��n�t|�t|�d�� ��� �k�r�|�|�� ��� }d}||k�rdtd|� d|� d�� | �d�  �q��ntt|�t|�d�� ��� �k�rZ|�|�� ��� }d}||k�rdtd|� d|� d�� | �d�  �q��n
t|�t|�d�� ��� �k�r�|�|�� ��� }d}||k�rdtd|� d|� d�� | �d�  �q��n�t|�t|�d�� ��� �k�r.|�|�� ��� }d}||k�rdtd|� d|� d�� | �d�  �q��n6t|�t|�d�� ��� �k�r�|�|�� ��� }d}||k�rdtd|� d|� d�� | �d�  �q�n�t|�t|�d�� ��� �k�r�|�|�� ��� }d}||k�rdtd|� d|� d�� | �d�  �q�nft|�t|�d�� ��� �k�rd|�|�� ��� }d}||k�rdtd|� d|� d�� | �d�  �q�t|�t|�d�� ��� �k�r�|�|�� ��� }d}||k�r�td|� d|� d�� | �d�  �q�q�t|�t|�d�� ��� �k�r.|�|�� ��� }d}||k�r�td|� d|� d�� | �d� q�t|�t|�d�� ��� �kr�|�|�� ��� }d}||kr�td|� d|� d�� | �d� q�| �d	� td|� d|� d�� W d   � n1 �s�0    Y  W n@ t�y�   td � Y n& t�y   t�  ttd! � Y n0 d S )"Nr   uM   [1;37m
             ==> [1;31m ^__^ أهلاً بكَ فى عالمى ^__^ zY<==

[1;37mGive me an encrypted word or hash and I will decrypt it
Happy Cracking ^__^ 
g�������?zEnter the hashed word: zGEnter the name of wordlist or press Enter to use the default wordlist: � zdb.txtg�������?�r)�mode�    z0[1;37m[[1;32m+[1;37m] Password found: [1;33mz2
[1;37m[[1;32m+[1;37m] Type of hash: [1;33mmd5�test�blake2bz/
[1;37m[[1;32m+[1;37m] Type of hash: [1;33m� �blake2s�sha1�sha224�sha256�sha384�sha512�sha3_224�sha3_256�sha3_384�sha3_512z"[[1;31m![0;37m] Sorry,But your (z/) is not match any word in the specified file (�)z9[1;37m[[1;31m![1;37m] The specified file is not existszExit :()r   �hashlibr   Zbannerr   r   r   r
   r   �open�strip�lenZmd5�encodeZ	hexdigestr   r   r   r    r!   r"   r#   r$   r%   r&   r'   �FileNotFoundError�KeyboardInterruptr	   r   )r   r)   Z
hashd_word�file�f�lineZhashd_word_in_fileZ	type_hashr   r   r   �hash_decrypter   s8   




 

�


 

�


 

�


 

�


 

�


 

�


 

�

 

�


 

�

 

�

 

�

 

�

 

�

�


�.r3   N)Zmymoduler   r3   r   r   r   r   �<module>   s    =
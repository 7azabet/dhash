a
    �l`�4  �                
   @   s:  d Z ddlmZ ddlT ddlmZ dZdZdZdZ	d	Z
dZd
ZdZdZddlmZ ddlZddlZddlZed� dZze�d� e�d� W n$ ey� Z zW Y dZ[n
dZ[0 0 dd� Zdd� Zdd� ZdZdZdd� ZdZdd� ZdZd d!� Z ee e e e e e! e" e# Z$d"d#� Z%e%�  d$d%� Z&e&�  dS )&z^
Who is '7azabet' ?
"7AZABET" is an Ethical Programmer not a hacker, Just a poor programmer .
�    )�sleep)�*)�tqdm�Ez[1;30m�[1;31mz[1;32mz[1;33mz[1;35mz[1;36m�[1;37m)�getpassNzChecking new version...�Kzgit pull; clear�clearc                   C   s   t �d� d S )Nr
   )�os�system� r   r   �encode/decrypter.pyr
   +   s    c                   C   s   t d� t�d� d S )NzWait..皙�����?)�print�timer   r   r   r   r   �wait/   s    r   c                   C   s   t d� d S )N� )r   r   r   r   r   �space4   s    r   �o� c                   C   sf   z<t td � t�d� t�d� t d� t�d� t�  W n$ ty`   t td � t	�  Y n0 d S )Nz$Checking Your Internet Connection...�   )zinformation-eg.blogspot.com�P   z[1;32m[+] You Are Connected�   z%[!] You Are Not Connected To Internet)
r   �Wr   r   �socketZcreate_connectionr
   �OSError�R�exitr   r   r   r   �test_connection@   s    



r   �lc               
   C   s�   zTt d�} td� | �� dks*| �� dkr2t�  n | dkrJtd� t�  ntd� W n, ty� } ztd� W Y d }~n
d }~0 0 d S )	Nz7[1;34mDo you wanna decrypt another hash (y/n): [1;33mr   Zyes�yr   z!Specify an option "yes" or "no" ?z[1;36mExiting, Goodbye :)z[0;91mERROR!)�inputr   �lower�hash_decrypter�again�	Exception)�aZexr   r   r   r%   P   s    r%   �rc                  C   s*   t td�dddddd�D ]} td� qd S )N�
   Fz
Progress..�itz#00FFFF)�asciiZdescZunit�totalZcolourg333333�?)r   �range�s)�_r   r   r   �probarb   s    r0   c                  C   s�   t t� � t�  t�d� t�  t dt� �� ttd t	 �} t
td t	 �}d}t�  | |kr�|tkr�t�d� t td � t�d� nt td	 � t�  d S )
Nzcat banner/login_banner.txtz


this is a test for s mes > z
USERNAME: z
PASSWORD: Z7AZABETg      �?z
[+] Done Successfully ^__^ r   z[!] NOT FOUND)r   r   r
   r   r   r   �pr"   r   r!   r   r0   r   r   �Gr   )�username�password�userr   r   r   �loginj   s    


r6   c            
      C   s�  dd l } dd l}dd l}td� t�  tdt� d�� | �d� tdt �}ttd t �}|dkrhd	}| �d
� dt	� d�D ]"}t
d� |j�|� |j��  q~t
d� �z�t|dd����}|D �]f}|�� }t|�dk�r$|�|�� ��� }||k�r�td|� d�� | �d� t�   �qR�n�t|�t|�d�� ��� �k�r�|�|�� ��� }d}	||k�r�td|� d|	� d�� | �d� t�   �qR�nXt|�t|�d�� ��� �k�r|�|�� ��� }d}	||k�r�td|� d|	� d�� | �d� t�   �qR�n�t|�t|�d�� ��� �k�rt|�|�� ��� }d}	||k�r�td|� d|	� d�� t�  | �d�  �qR�nxt|�t|�d�� ��� �k�r�|�|�� ��� }d}	||k�r�td|� d|	� d�� t�  | �d�  �qR�nt|�t|�d�� ��� �k�rT|�|�� ��� }d}	||k�r�td|� d|	� d�� t�  | �d�  �qR�n�t|�t|�d�� ��� �k�r�|�|�� ��� }d}	||k�r�td|� d|	� d�� t�  | �d�  �qR�n(t|�t|�d�� ��� �k�r4|�|�� ��� }d}	||k�r�td|� d|	� d�� t�  | �d�  �qR�n�t|�t|�d�� ��� �k�r�|�|�� ��� }d}	||k�r�td|� d|	� d�� t�  | �d�  �qR�nHt|�t|�d�� ��� �k�r|�|�� ��� }d}	||k�r�td|� d|	� d�� t�  | �d�  �qRn�t|�t|�d�� ��� �k�r�|�|�� ��� }d }	||k�r�td|� d|	� d�� t�  | �d�  �qRnlt|�t|�d�� ��� �k�r�|�|�� ��� }d!}	||k�r�td|� d|	� d�� t�  | �d�  �qRt|�t|�d�� ��� �k�rZ|�|�� ��� }d}	||k�r*td|� d|	� d�� t�  | �d�  �qRq�t|�t|�d�� ��� �k�r�|�|�� ��� }d}	||k�r*td|� d|	� d�� t�  | �d�  �qRq�t|�t|�d�� ��� �kr�|�|�� ��� }d}	||kr�td|� d|	� d�� t�  | �d� q�| �d� td"|� d#|� d$�� t�  W d   � n1 �sh0    Y  W n@ t �y�   td%� Y n& t!�y�   t"�  tt#d& � Y n0 d S )'Nr   r   uI   [1;37m             ==>[1;31m ^_^ أهلاً بكَ فى عالمى ^_^ z[<==


[1;37mGive me an encrypted word or hash and I will decrypt it
Happy Cracking ^__^ 

g�������?zEnter the hashed word: zGEnter the name of wordlist or press Enter to use the default wordlist: r   zdb.txtg      �?�
zCracking...
r   r   r(   )�mode�    z0[1;37m[[1;32m+[1;37m] Password found: [1;33mz2
[1;37m[[1;32m+[1;37m] Type of hash: [1;33mmd5�test�blake2bz/
[1;37m[[1;32m+[1;37m] Type of hash: [1;33mr   �blake2s�sha1�sha224�sha256�sha384�sha512�sha3_224�sha3_256�sha3_384�sha3_512z"[[1;31m![0;37m] Sorry,But your (z/) is not match any word in the specified file (�)z9[1;37m[[1;31m![1;37m] The specified file is not existszExit :()$r   �hashlib�sysr   Zbannerr   r   r"   r2   �Cr.   �stdout�write�flush�open�strip�lenZmd5�encodeZ	hexdigestr%   r;   r<   r=   r>   r?   r@   rA   rB   rC   rD   rE   �FileNotFoundError�KeyboardInterruptr   r   )
r   rG   rH   Z
hashd_word�file�c�f�lineZhashd_word_in_fileZ	type_hashr   r   r   r$   �   sf   
�





 

�


 

�


 

�


 

�


 

�


 

�


 

�


 

�


 

�

 

�

 

�

 

�

 

�


�


�
*r$   )'�__doc__r   r   r.   Zmymoduler   ZfcZblackr   r2   r!   �b�PrI   r   r   r   r   r   Zfocr   r&   �errr
   r   r   ZficZtcr   Zscr%   Zsicr0   ZsecZeicZncr1   r6   r$   r   r   r   r   �<module>   sN   
$ F
a
    �%�_�  �                   @   sd   d Z dZdZdZdZdZdZdZddlZddl	Z	ddl
Z
d	d
� Zdd� Zdd� Zdd� Zdd� ZdS )z[1;30mz[1;31mz[1;32mz[1;33mz[1;35mz[1;36mz[1;37m�    Nc                   C   s   t �d� d S )N�clear)�os�system� r   r   �3/root/Desktop/7azabet/decrypt_hash_tool/mymodule.pyr      s    r   c                   C   s   t d� t�d� d S )NzWait..g�������?)�print�time�sleepr   r   r   r   �wait   s    r
   c                   C   s   t d� d S )N� )r   r   r   r   r   �space   s    r   c                   C   s   t �  t�d� d S )Nzcat banner/El_Korsan_tool.txt)r   r   r   r   r   r   r   �banner   s    r   c                   C   sf   z<t td � t�d� t�d� t d� t�d� t�  W n$ ty`   t td � t	�  Y n0 d S )Nz$Checking Your Internet Connection...�   )zinformation-eg.blogspot.com�P   z[1;32m[+] You Are Connected�   z%[!] You Are Not Connected To Internet)
r   �Wr   r	   �socketZcreate_connectionr   �OSError�R�exitr   r   r   r   �test_connection#   s    



r   )Zblackr   �G�y�b�P�Cr   r   r   r   r   r
   r   r   r   r   r   r   r   �<module>   s   
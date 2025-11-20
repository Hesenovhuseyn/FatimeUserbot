MESAJ="𝐅𝐚𝐭𝐢𝐦𝐞 𝐔𝐬𝐞𝐫𝐛𝐨𝐭 ᥫ᭡ S T R I N G SESSION"
MESAJ+="\nTelegram: @HuseynH"
pkg upgrade
clear
echo -e $MESAJ
echo "Python yüklənir..."
pkg install python -y
clear
echo -e $MESAJ
echo "TeleThon yüklənir..."
pip install telethon
echo "Requests/BS4 yüklənir..."
pip install requests
pip install bs4
clear
echo -e $MESAJ
echo "Fayl yazılır..."
curl "https://raw.githubusercontent.com/Hesenovhuseyn/FatimeUserbot/master/FatimeUb.py" --output "FatimeUb.py"
clear
echo -e $MESAJ
echo "Qurulum Bitdi! İndi String Ala Bilərsiz."
clear
python FatimeUb.py

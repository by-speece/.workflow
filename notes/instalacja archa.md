# Instalacja Archa z szyfrowaniem
## Przygotowywanie
Oczywiście przed rozpoczęciem tych kroków należy połączyć się z internetem

- `timedatectl status` - sprawdzamy czy data,godzina się zgadza
- `timedatectl set-ntp true`- synchronizujemy jeśli jest błędne ustawienie

## Partycjonowanie
Tworzymy partycje według własnego uznania na moim przykładzie będzie to wygląd następujący:

- `sda1` - 1gb - Type: EFI
- `sda2` - 4gb - Type: Swap
- `sda3` - Reszta - Type Linux

Za pomocą polecenia `lsblk` możemy skontrolować nasze partycje

### Formatowanie

- `mkfs.fat -F32 /dev/sda1` - formatujemy partycje
- `mkswap /dev/sda2` - tworzymy format swap
- `swapon /dev/sda2` - aktywujemy swap
- `cryptsetup luksFormat -v  -s 512 -h sha512 /dev/sda3` - Tworzymy Zaszyfrowaną Partycje 

By otworzyć partycję zaszyfrowaną musimy użyć następującej komendy:

- `cryptsetup open /dev/sda3 main` - main można zastąpić dowolną inną nazwą(jest to nasza nazwa)
- `mkfs.ext4 /dev/mapper/main` - formatujemy naszą zaszyfrowaną partycję

## Etap końcowy
By móc bez problemu uruchomić system musimy wprowadzić jedną rzecz w grubie.
- `blkid` - sprawdzamy UUID naszej zaszyfrowanej partycji(sda3 w moim przypadku)
Za pomocą `ls /dev/disk/by-uuid/[tu numery naszego UUID]` uzyskujemy czystą ścieżkę
- `vim /etc/default/grub`
Zmieniamy linię `GRUB_CMDLINE_LINUX` tak by wglądała następująco `GRUB_CMDLINE_LINUX="cryptodevice=[ścieżka do partycji:nazwa którą przypisaliśmy]:allow-discards"`
Usuwamy komentarz w linii `#GRUB_ENABLE_CRYPTODISK=y` 
Następnie przechodzimy do edycji `mkinitcpio.conf`
- `vim /etc/mkinitcpio.conf`
W linii `MODULES=()` dodajemy `ext4`, natomiast w `HOOKS=()` dodajemy `encrypt`.
- `mkinitcpio -p linux` - budujemy obraz
- `grub-install --target=x86_64-efi --bootloader-id=grub_uefi --recheck --efi-directory=/boot`
- `grub-mkconfig -o /boot/grub/grub.cfg`


## UEFI Interactive Shell

`ls FSO:\EFI\grub_uefi\grubx64.efi` - sprawdzamy czy nasza ścieżka istnieje
`edit startup.nsh` - edytujemy

Dodajemy ścieżkę powyżej czyli efekt końcowy powinien wyglądać następująco:

`FSO:\EFI\grub_uefi\grubx64.efi`

FROM archlinux:latest

RUN pacman -Suy --noconfirm
RUN  pacman -S --noconfirm ponysay
ENTRYPOINT ["/usr/bin/ponysay"]
CMD ["Hey, netology”]
pkgname=wordminal
pkgver=1.0.0
pkgrel=1
pkgdesc="A terminal-based word guessing game in Python"
arch=('any')
url="https://github.com/ChipishGames/Wordminal"
license=('MIT')
depends=('python')
source=("$pkgname::git+$url.git")
md5sums=('SKIP')

package() {
    install -Dm755 "$srcdir/$pkgname/main.py" "$pkgdir/usr/bin/wordminal"
    install -Dm644 "$srcdir/$pkgname/word-list.txt" "$pkgdir/usr/share/wordminal/word-list.txt"

    # Create a launcher script to ensure the word list is found
    echo "#!/bin/sh
WORDLIST=\"/usr/share/wordminal/word-list.txt\"
exec python /usr/bin/wordminal \"\$@\"" > "$pkgdir/usr/bin/wordminal"


    chmod +x "$pkgdir/usr/bin/wordminal.sh"
    mv "$pkgdir/usr/bin/wordminal.sh" "$pkgdir/usr/bin/wordminal"
}

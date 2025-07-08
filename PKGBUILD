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
    install -Dm644 "$srcdir/$pkgname/word-list.txt" "$pkgdir/usr/share/wordminal/word-list.txt"

    # Write launcher script to $pkgdir/usr/bin/wordminal
    install -Dm755 /dev/stdin "$pkgdir/usr/bin/wordminal" << 'EOF'
#!/bin/sh
exec python /usr/lib/wordminal/main.py "$@"
EOF

    # Install actual Python script to a non-bin location
    install -Dm755 "$srcdir/$pkgname/main.py" "$pkgdir/usr/lib/wordminal/main.py"
}

sublime-text-user-settings
========================

My personal Sublime Text 3 User Settings. Take a look at [sublime-text-user-settings/User/Package Control.sublime-settings](https://github.com/striderkein/sublime-text-user-settings/blob/master/User/Package%20Control.sublime-settings) for a list of my installed packages


# Install/Update
```sh
$ rm -rf ~/Library/Application \Support/Sublime\ Text\ 3/Users
$ git clone https://github.com/striderkein/sublime-text-user-settings.git ~/Library/Application\ Support/Sublime\ Text\ 3/Users
```

# 独自プラグインについて
- code_point.py
  選択した1文字について、SJIS, EUC-JP, UTF-8, Unicode(UTF-16) のコードポイントおよび Unicode name を表示するプラグイン。 
  [参考にしたサイト](http://kaerouka.hatenablog.com/entry/2014/03/25/055617)

  使い方
  Sublime Text で任意の1文字を選択（ハイライト）する。
  command + shift + p でコマンドパレットを開き `code_point` と入力する。

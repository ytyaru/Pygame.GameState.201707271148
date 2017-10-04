# このソフトウェアについて

ゲームコマンドクラスを作った。

作り方次第でStateSwitcher.pyとGameState.pyで循環インポートしてしまう。metaclassの実装に変更したせいで生じてしまった。metaclassでは循環インポートが生じやすいかも知れない。

# 開発環境

* Linux Mint 17.3 MATE 32bit
* [pyenv](https://github.com/pylangstudy/201705/blob/master/27/Python%E5%AD%A6%E7%BF%92%E7%92%B0%E5%A2%83%E3%82%92%E7%94%A8%E6%84%8F%E3%81%99%E3%82%8B.md) 1.0.10
    * Python 3.6.1
        * [PyGame](http://ytyaru.hatenablog.com/entry/2018/06/11/000000) 1.9.3
        * [PyGame Utilities(pgu)](http://ytyaru.hatenablog.com/entry/2018/06/19/000000) 0.18
        * [PyOpenGL](http://ytyaru.hatenablog.com/entry/2018/06/15/000000) 3.1.0
        * PyOpenGL_accelerate 3.1.0
        * PyOpenGL_Demo 3.0.0
        * [Pillow](https://pillow.readthedocs.io/en/4.2.x/) 4.2.1
        * [NumPy](http://www.numpy.org/) 1.13.1

# 実行

```sh
$ python Main.py
```

Enter, Space, Zキーのいずれかでゲーム状態が変化する。各ゲーム状態ごとに画面の色が変わる。ESCキーまたはAlt+F4で終了する。

# 概要

あみだくじゲーム。

## パッケージ分け

ざっくり分けた。分類に正確性はない。

階層|パッケージ|説明
----|----------|----
1|framework|ソースコードの構成を整えるためのコード群。(デザパタ等)
2|ui|ユーザインタフェース部分。(pygame等)
3|game|ゲームの本質に関わるコード群。(本ゲーム固有)

階層が低いほどプログラミングに関する部分。高いほどユーザ側(ゲーム的)な部分。

### 一覧

* src/
    * framework/
        * state/
            * StateSwitcher.py
            * GameState.py
            * SelectState.py
            * AnimateState.py
            * ResultState.py
    * ui/
        * Screen.py
        * CalcSize.py
    * game/
        * Ghostleg.py
        * LinesAnimation.py

## フレームワーク

ゲーム状態が切り替わるときに特定の処理を実行するフレームワークメソッドを追加した。

各ステータスごとに開始処理、終了処理を実装させる。それをSwitcherクラスで呼び出す。そのフレームワークを実装した。

フレームワークで実装すべき内容はゲームコマンドである。

### ゲームコマンド

ゲーム固有のプログラミング処理のことを指す。

コマンド|説明
--------|----
あみだくじ新規作成|初回、結果表示からの再開のときに新しいあみだくじを作成する。
アニメーション開始|あみだくじで線を選択後、アニメーションを開始する。
アニメーション完了|アニメーション最中でも強制的に完了した状態にする。（座標の頂点リストを瞬時に完成させる）
結果演出開始|あみだくじのアニメーション完了後、効果音など何らかの演出をする。
結果演出終了|たとえば効果音などが鳴っている最中なら消す。

未実装である。ゲームコマンドの呼出元では実行に必要なクラスや引数などを隠蔽したい。専用のクラスを作ることになるだろう。

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

Library|License|Copyright
-------|-------|---------
[pygame](http://www.pygame.org/)|[LGPL](https://www.pygame.org/docs/)|[pygame](http://www.pygame.org/)


<h1><font color="Crimson">SelectedAnimeView（機能のみ）</font></h1>

<h2><font color="aqua">使用技術</font></h2>
<hr>
<ul>
    <li>Python3
    <li>Flask
    <li>MySQL
    <li>HTML
    <li>CSS
</ul>

<h2></h2>

<h2><font color="aqua">概要</font></h2>
<hr>
MySQLにあるアニメの情報を取得して、静的データとして保存されている画像を組み合わせて一覧画像を生成します。<br>
表示されているアニメを選択して、一覧画像に情報として反映します。<br>

※機能だけ実装した状態の画像


<img src="GAB\sample_1.png" width=30% height=30%> <br>
<img src="GAB\sample_2.png" width=30% height=30%> <br>
<img src="GAB\sample_3.png" width=30% height=30%> <br>

<h2><font color="aqua">必要事項</font></h2>
<hr>
<ul>
    <li>MySQLにデータの格納
    <li>静的データの用意（個別のアニメ情報の画像）
</ul>

<h2>ディレクトリ構造</h2>
<hr>
GAB/<br>
|- Datasotre/<br>
|- static/<br>
|　 ｜└ css/<br>
|　 ｜　└ anime_generator.css<br>
| 　└ spring_2021/<br>
|　 └ winter_2021/<br>
|- templates/<br>
| 　└ anime_generator.html<br>
| 　└ base.html<br>
| 　└ generator_result.html<br>
| 　└ main.html<br>
|- index.py<br>
|- make_pic.py<br>


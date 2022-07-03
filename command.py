<!DOCTYPE html>
<html>
    <head>
        <title>Madako</title>
        <meta charset="UTF-8" />
        <link href="https://fonts.googleapis.com/css?family=Josefin+Sans" rel="stylesheet">
        <style>
            html,body
{
    padding:0;
    margin:0;
    max-width:100%;
    user-select:none;
    -ms-user-select:none;
    -moz-user-select:none;
    -webkit-user-select:none;


}



.nice-font
{
    font-family:'Josefin Sans',sans-serif;
}

header
{
      text-align:center;
}

main
{
    padding:10px;
    margin-bottom:50px;
}

footer #command
{
    position:fixed;
    bottom:0;
    width:100%;
    padding:7px 7px;
    padding-right:7px;
    margin-bottom:5px;
    border-radius:20px;
    border:0.5px solid #9e9e9e50;
    -ms-box-sizing:border-box;
    box-sizing:border-box ;
    background-color:#fff;

}

#command input
{
    display:block;
    width:73%;
    float:left;

}

#command input,#command button
{

    padding:10px 15px;
    border:0;
    outline:0;
}


button
{
    background-color:#1e88e5;
    color:#fff;
    border-radius:20px;
    font-weight:300;
    float:right;


 }

 .row
 {
     width:100%;
     margin-bottom:10px;
     display:block;
 }
 .row::after{
      content: "";
    display: table;
    clear: both;
 }

.chat
{
    border:0.7px solid #9e9e9e50;
    word-wrap:break-word;
    background-color:#fff;
    border-radius:20px;
    color:#333;
    padding:10px 20px;
    display:inline-block
}

.question
{
    float:right;
    background-color:#1e88e5;
    color:#fff;
    border-color:rgba(0,0,200,0.1);
}

.answer
{
    float:left;
}


        </style>

        <script>

const Random = list => list[Math.floor(Math.random()*list.length)];

const Links = {
    "radio" : "radio",
    "facebook" : "https://www.facebook.com",
    "google" : "https://www.google.com",
    "twitter" : "https://www.twitter.com",
    "panduancode" : "https://www.panduancode.com"
};

const getLink = siteName => `klik disini untuk membuka panduancode <a href="${Links[siteName]}">${siteName}</a>`;



const pertanyaan = [

    `Gunakan pertanyaan yang mengandung kata kunci, contoh kata kunci (pembuat mu) dan pertanyaan yang dapat di ajukan adalah (siapa pembuat mu Anisa?) dan lain-lain.<br/>
Daftar kata kunci yang dapat di pakai:<br/>
1.Siapa pembuat mu<br/>
2.umur kamu berapa<br/>
3.apakabar<br/>
4.hi<br/>
5.kamu sedang apa<br/>
6.siapa saya<br/>
7.stmj pangkat 3<br/>
8.nama mu<br/>
9.ulang tahun mu<br/>
10.tanggal<br/>
11.jam<br/>
12.kamu mau hadiah apa<br/>
13.makan kesukaan mu<br/>
14.minuman kesukaan mu<br/>
15.sudah makan<br/>
16.selamat malam<br/>
17.selamat pagi<br/>
18.selamat siang<br/>
19.selamat sore<br/>
20.dimana kamu<br/>
21.aku boleh kesana<br/>
22.i love you<br/>
23.aku suka kamu<br/>
24.kamu sedang dimana<br/>
25.lol<br/>
26.cepet mandi<br/>
27.aku jemput<br/>
28.berangkat<br/>
29.panduancode<br/>
30.facebook<br/>
31.google<br/>
32.twitter<br/>
33.sampai jumpa<br/>`

];

const ini_adalah_daftar_pertanyaan_yang_dapat_Anda_gunakan = pertanyaan => Random(pertanyaan);


const Message = () => alert("hehe,halo~! ");

const illegals = [
  "window",
  ...Object.keys(window),
  ...Object.keys(document),
  ...Object.keys(Element.prototype)
];

const isLegal = string => {

    let Legal = true;

    illegals.forEach(illegal=>{

        if(string.indexOf(illegal) !== -1)
        {
            Legal = false;
        }

    });

    return Legal;
}

const HtmlSpecialChars = function(string) {

    let escapedString = string;


     const len = HtmlSpecialChars.specialchars.length;

    for (let x = 0; x < len; x++) {

   escapedString = escapedString.replace( new RegExp(HtmlSpecialChars.specialchars[x][0], 'g'), HtmlSpecialChars.specialchars[x][1] );
        }

    return escapedString;
};

HtmlSpecialChars.specialchars = [
    [ '&', '&amp;' ],
    [ '<', '&lt;' ],
    [ '>', '&gt;' ],
    [ '"', '&quot;' ]
];

const monthNames = [
    "Januari",
    "Februari",
    "Maret",
    "April",
    "Mei",
    "Juni",
    "Juli",
    "Agustus",
    "September",
    "Oktober",
    "November",
    "Desember"
 ];


const today = monthNames =>
{
  let date = new Date();

  return `${monthNames[date.getMonth()]} ${date.getDate()}, ${date.getFullYear()}`;

}


const now = () =>
{
    let date = new Date();

    return date.toLocaleTimeString();
}

const Evaluate = expression =>
{
    try
    {
        if(isLegal(expression))
        {


            const result = eval(HtmlSpecialChars(expression));
            return result;

        }
        else
        {
            return "error";
        }
    }

    catch(err)
    {
        return "error";
    }
}

const Answers = {
    "pertanyaan" : ini_adalah_daftar_pertanyaan_yang_dapat_Anda_gunakan(pertanyaan),
      "pembuat mu" : "Saya dibuat oleh siapa hayo? :)",
    "umur kamu berapa" : "ngapain tanya umur om?~.",
    "umurmu" : "ngapain tanya umur om?~.",
    "umur" : "ngapain tanya umur om?~.",
    "radio" : "kamu bisa mendengarkan radio yang tersedia pada laman perpustakaan digital atau pada laman radio, atau atau klik pada teks berwarna biru berikut  <a href='https://sman4muarateweh.sch.id/radio' target='_blank'>Radio</a>",
    "komik" : "kamu bisa membaca komik yang tersedia pada laman perpustakaan digital atau eperpus.",
    "segs" : "astafirullah..",
    "illya" : "eh?!!!!!!",
    "ilya" : "eh?!!!!!!",
    "madako" : "oh madako,madako tersedia pada channel group telegram SMAN 4 Muara Teweh,silahkan untuk ke <a href='https://t.me/smafourmute' target='_blank'> klik disini</a> laman telegram SMAN 4 Muara Teweh  atau <a href='https://t.me/madakobot' target='_blank'> klik disini</a> untuk tanya madako langsung.  ",


    "sejarah" : "sejarah SMAN 4 Muara Teweh silahkan cek pada laman wikipedia atau klik laman berikut   <a href='https://id.wikipedia.org/wiki/SMA_Negeri_4_Muara_Teweh' target='_blank'>Sejarah</a>  ",
    "hentai" : "astafirullah..",
    "waifu kepsek" : "sagiri om katanya..",
    "waifu kepala sekolah" : "sagiri om katanya..",
    "waifu pak mario" : "rahasia negara..",
    "kepsek" : "Kepala Sekolah kami adalah Bapak Taryana,kamu dapat menghubunginya dengan mengkontaknya melalui kontak yang sudah disediakan pada laman kepsek/kepala sekolah~",
    "kepala sekolah" : "Kepala Sekolah kami adalah Bapak Taryana,kamu dapat menghubunginya dengan mengkontaknya melalui kontak yang sudah disediakan pada laman kepsek/kepala sekolah~",
    "umur kamu berapa" : "6570 Hari :) ~.",
    "apakabar" : "aku baik-baik saja %U% 😃. kalau kamu bagaimana ? ",
    "halo" : "Halo %U% ",
    "hi" : "Hi %U% ",
    "kamu sedang apa" : "sedang segs",
    "siapa saya" : " %U% kok tanya saya ? ,kamu sehat?",
    "stmj pangkat 3" : "STMJ Pangkat 3 ( Semester 6 Masih Jomblo, Semester 7 Masih Jomblo, Sampai Tamat Masih Jomblo, Dan Pada Akhirnya Loe Sadar Betapa Indahnya Merasakan Cinta 😂😂😂",
    "nama mu" : "kepo ih~",
    "namamu" : "Kepo ih~",
    "nama mu?" : "Kepo ih~",
    "namamu?" : "Kepo ih~",
    "ultahmu" : "ulang tahun ku tanggal 8 Maret , emangnya kenapa nanya kapan ulang tahun ku? mau ngasih hadiah? ,tch ningen",
    "ultahmu?" : "ulang tahun ku tanggal 8 Maret , emangnya kenapa nanya kapan ulang tahun ku? mau ngasih hadiah? ,tch ningen",
    "ulang tahun mu" : "ulang tahun ku tanggal 8 Maret , emangnya kenapa nanya kapan ulang tahun ku? mau ngasih hadiah? ,tch ningen",
    "tanggal" : "sekarang "+ today(monthNames) + " %U% ",
    "jam" : "sekarang jam " + now('hh') + " %U%",


    "kamu mau hadiah apa" : "Ehh gak usah aku bercanda kok tapi ya kalau mau ngasih hadiah aku mau kamu pergi dari hidup ku bisa? %U% 😂",
    "makanan kesukaan mu" : "aku bukan human , jadi tolong pertanyaan yang robot-siawi,tch ningen..",
    "minuman kesukaan mu" : "aku bukan human , jadi tolong pertanyaan yang robot-siawi,tch ningen..",
    "NGENTOD" : "sudah kubilang jangan toxic KONSOL~!.",
    "ngentod" : "sudah kubilang jangan toxic KONSOL.",
    "sudah makan" : "belum.",
    "sudah makan?" : "belum.",
    "selamat malam" : "selamat malam juga %U%",
    "selamat pagi" : "selamat pagi juga %U%",
    "selamat siang" : "selamat siang juga %U%",
    "selamat sore" : "selamat sore juga %U%",
    "dimana kamu" : "saya sedang di Taman dekat Air mancur 7 rupa %U%. 😃",
    "aku boleh kesana" : "gak boleh, aku mau sendiri.",
    "i love you" : "I Love you too %U% 😊",
    "aku suka kamu" : "hmm aku juga suka kamu kok 😊",
    "kamu sedang dimana" : "saya sedang di rumah",
"lol" : "Haha.. That was funny 😂",
"cepet mandi" : "mau apa?",
"aku jemput" : "iya deh aku tunggu sekarang",
"berangkat" : "jangan telat ya",
"sampai jumpa" : "sampai jumpa kembali %u%",

};


const Notfound = "Jujurly aku tidak understand,kamu say what?";

const Invalid = "hah?!";


const D = window.document;

const element = selector => D.querySelector(selector);

const Answer = (Main,User,Text) =>
{
    let Flag = false;

    const Result = Evaluate(Text);

    text = Text.toLowerCase();

    Object.keys(Answers).forEach(key =>{

    if(!Flag)
    {
        if(text.indexOf(key) !== -1 )
        {

          addAnswer(
              Main,
              Answers[key].replace(
              "%U%",
              User
              )
          );

          Flag = true;

       }

       else if(typeof Result == "number")
       {

             addAnswer(
                 Main,
                 `${Text} equals ${Result}`
             );

             Flag = true;

       }

       }

    });

    if(!Flag)
    {
        addAnswer(Main,Notfound);
    }


};

const addQuestion = (Main,text) =>
{
    Main.innerHTML += `
        <div class="row">
            <div class="chat question">${text}</div>
        </div>
    `;
}

const addAnswer = (Main,text) =>
{
    Main.innerHTML += `
    <div class="row">
        <div class="chat answer">${text}</div>
    </div>
    `;
}


D.addEventListener("DOMContentLoaded",()=>{

    const Main = element("main");

    const Askbtn = element("button");

    const Question = element("input");

    const Lastdiv = element("#last");

    let User = prompt("Siapa namamu ?");

    while(User === null  || User === '')
    {

        User = prompt("Tolong beritahu aku,siapa namamu? >:v  ");

    }

    Question.focus();

    const Ask = () =>{

        const Text = Question.value;

        if(Text.length)
        {

            addQuestion(Main, Text);

            Question.value = "";

            Answer(Main,User,Text);

            Lastdiv.scrollIntoView();

        }
    };


    Askbtn.addEventListener("click",Ask);

    Question.addEventListener("keyup",function(event){
        if(event.keyCode === 13)  Ask();
    });

    addAnswer(Main,`Halo! ${User}.. ,selamat datang di situs SMAN 4 Muara Teweh , ada yang bisa kubantu? ~,tolong jangan ngomong toxic dan cabul seperti dwi_ganteng :) <br> <img src="img/0.gif" width="150" height="150"><br>`);

    Message();
});

        </script>
    </head>
    <body>
        <header>
            <h1 class="nice-font" ></h1>
        </header>

        <main class="nice-font">

        </main>

        <div id="last"></div>

        <footer>
            <div id="command">
                <input placeholder="masukkan pesan disini dan klik kirim ~ ..." type="text" />
                <button class="nice-font">Kirim</button>
            </div>
        </footer>

    </body>
</html>

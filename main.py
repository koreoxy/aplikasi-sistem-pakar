import PySimpleGUI as sg

#sg.theme('default1')
sg.theme('DarkGreen6')
# sg.theme('LightBrown3')
# sg.theme('Tan')

# VARIABLE
title_table_pasien = ['Nama', 'Tanggal Lahir', 'Alamat Rumah', 'Nomor Telepon', 'Hasil Diagnosa']
data_pasien = [['Budi', '1-10-1999', 'Meulaboh', '08526071882', 'Penyakit Eksim']]


title_penyakit_kulit = ['Kode', 'Nama Penyakit Kulit']
data_penyakit_kulit = [
    ['P01', 'Eksim'],
    ['P02', 'Dermatitis'],
    ['P03', 'Impetigo'],
    ['P04', 'Jerawat'],
    ['P05', 'Kudis'],
    ['P06', 'Kurap'],
    ['P07', 'Panu'],
    ['P08', 'Lichen Planus'],
    ['P09', 'Hives'],
]
title_gejala = ['Kode Gejala', 'Nama Gejala']
data_gejala = [
    ['G01', 'Rasa Panas dan dingin yang berlebihan pada bagian kulit yang terkena eksim.'],
    ['G02', 'Rasa gatal terutama terasa pada malam hari.'],
    ['G03', 'Tampak lepuhan-lepuhan kecil dan kulit bersisik yang keras pada permukaan kulit yang akan \ndisertai dengan pembengkakan.'],
    ['G04', 'Kulit kering, bersisik, kemerah-merahan.'],
    ['G05', 'Timbul bintil-bintil yang mengandung air atau nanah.'],
    ['G06', 'Ruam kemerahan.'],
    ['G07', 'Peradangan.'],
    ['G08', 'Gatal yang kadang-kadang terasa parah.'],
    ['G09', 'Kering.'],
    ['G10', 'Pembengkakan.'],
    ['G11', 'Kulit kering.'],
    ['G12', 'Bersisik.'],
    ['G13', 'Lecet melepuh.'],
    ['G14', 'Menebal.'],
    ['G15', 'Pecah-pecah.'],
    ['G16', 'Kulit melepuh dan berisi cairan.'],
    ['G17', 'Pecahan kulit yang melepuh dan berwarna kuning.'],
    ['G18', 'Munculnya bercak merah menyerupai luka yang tidak terasa sakit, namun gatal.'],
    ['G19', 'Bercak bisa menyebar dalam waktu singkat ketika disentuh atau digaruk, kemudian berganti \nmenjadi kerak berwarna kecokelatan.'],
    ['G20', 'Munculnya bintik-bintik.'],
    ['G21', 'Kulit berminyak.'],
    ['G22', 'Sakit atau panas apabila disentuh.'],
    ['G23', 'Gatal yang sangat terasa pada permukaan kulit.'],
    ['G24', 'Berwarna kemerahan dan biasanya disertai infeksi lanjutan seperti yang diakibatkan oleh \nbakteri maupun jamur.'],
    ['G25', 'Bisul pada telapak tangan atau kaki.'],
    ['G26', 'Ruam kemerahan yang berbentuk cincin dengan garis luar yang tidak beraturan.'],
    ['G27', 'Ruam terasa bersisik dan gatal.'],
    ['G28', 'Lingkaran ruam kurap juga dapat melebar dan muncul di bagian tubuh mana saja.'],
    ['G29', 'Ruam membentuk benjolan dan melepuh.'],
    ['G30', 'Kulit pecah-pecah di bagian yang terinfeksi serta kulit bersisik.'],
    ['G31', 'Ruam yang gatal, kering, dan terkelupas di antara jari kaki.'],
    ['G32', 'Rasa gatal ketika berkeringat dan warna sebagian kulit berubah menjadi putih.'],
    ['G33', 'Terdapat sisik halus yang menutupinya.'],
    ['G34', 'Benjolan berwarna ungu kemerahan dengan bagian atas yang rata dan mengkilat.'],
    ['G35', 'Terbentuknya sebagian kulit yang menebal dan bersisik, biasanya di sekitar pergelangan kaki.'],
    ['G36', 'Terasa gatal.'],
    ['G37', 'Perubahan warna kulit menjadi gelap setelah benjolan-benjolan mereda.'],
    ['G38', 'Adanya warna merah pada kulit serta ruam gatal.'],
    ['G39', 'Gatal-gatal disertai kemerahan pada kulit.'],
    ['G40', 'Busung.'],
    ['G41', 'Kulit terasa panas.'],
    ['G42', 'Pembengkakan yang berlebihan dari kelopak mata.'],
    ['G43', 'Kesulitan bernafas atau menelan.'],
]

title_aturan = ['Rule', 'IF', 'THEN', 'Keterangan']
data_aturan = [
    ['1', 'G01,G02,G03,G04,G05', 'P01', 'Eksim'],
    ['2', 'G06,G07,G08,G09,G10,G11,G12,G13,G14,G15', 'P02', 'Dermatitis'],
    ['3', 'G16,G17,G18,G19', 'P03', 'Impetigo'],
    ['4', 'G20,G21,G22', 'P04', 'Jerawat'],
    ['5', 'G23,G24,G25', 'P05', 'Kudis'],
    ['6', 'G26,G27,G28,G29,G30,G31', 'P06', 'Kurap'],
    ['7', 'G32,G33', 'P07', 'Panu'],
    ['8', 'G34,G35,G36,G37', 'P08', 'Lichen Planus'],
    ['9', 'G38,G39,G40,G41,G42,G43', 'P09', 'Hives']
]

solusi_penyakit_eksim = [
    'Pengobatan Eksim \n Dipercaya jika belum ada obat yang dapat mengatasi eksim. Perawatan terhadap kondisi ini bertujuan untuk menyembuhkan kulit yang terserang serta mencegah gejalanya. Pengobatan yang dapat dilakukan berdasarkan berbagai faktor. berikut beberapa cara pengobatan yang bisa dilakukan:\n\n Pengobatan rumahan\n Ada beberapa perawatan rumahan yang bisa dilakukan untuk mengatasi eksim, yaitu: \n- Mandi dengan air hangat. \n- Mengoleskan pelembap setelah mandi. \n- Menggunakan pelembap setiap hari. \n- Memakai katun dan kain lembut. \n- Menghindari bahan pakaian yang kasar, gatal, serta pakaian yang ketat. \n- Menggunakan pelembap udara dalam cuaca yang kering atau dingin. \n- Menghindari pemicu terjadinya eksim. \n\n Dan jika Pengobatan rumahan ini tidak berhasil anda harus konsultasi ke dokter spesialis kulit di rumah sakit yang ada di sekitar tempat tinggal anda.'
]


info_penyakit_eksim =[
    '  Eksim adalah istilah terkait gangguan pembengkakan pada kulit. Gangguan ini disebut juga dengan dermatitis. Saat terjadi, reaksi alergi pada kulit dapat ditandai dengan timbulnya warna kemerahan, ruam, dan rasa gatal. Kondisi ini dapat menimbulkan rasa tidak nyaman serta mengganggu penampilan.\n  Eksim bukan penyakit yang menular dan sejauh ini penyebabnya belum diketahui. Kemungkinan besar terjadi akibat adanya faktor genetik dan lingkungan. Seseorang yang mengidap demam dan asma biasanya juga memiliki penyakit ini. Penyakit yang disebut dermatitis ini juga dapat menjadi penyakit yang dapat bertahan lama.\n\nGejala Eksim :\n   Semua orang dapat mengalami eksim tanpa terkecuali, dari orang dewasa hingga anak-anak. Gejalanya pun dapat muncul sejak seseorang usianya sudah di atas dua tahun. Eksim bisa menghilang seiring bertambahnya usia, tetapi juga bisa menjadi penyakit seumur hidup.\nNah, gejala eksim paling umum yang dapat timbul saat gangguan ini terjadi adalah : \n  - Kulit yang menjadi kering dan bersisik.\n  - Kulit yang memerah.\n  - Terasa gatal.\n  - Luka yang terbuka atau berkerak.\n\nGejala eksim pada Bayi :\nSaat gangguan kulit ini terjadi pada bayi yang usianya di bawah dua tahun, beberapa gejala yang timbul, antara lain :\n  - Timbulnya ruam di kulit kepala dan pipi.\n  - Ruam yang menggelembung sebelum mengeluarkan cairan.\n  - Ruam yang menimbulkan rasa gatal sehingga tidurnya terganggu.\n\nGejala eksim untuk anak yang lebih besar :\nGejala yang timbul saat masalah ini terjadi pada anak berusia dua tahun ke atas dapat berbeda dengan bayi. Berikut beberapa gejalanya :\n  - Ruam terlihat pada lipatan siku atau lutut.\n  - Ruam muncul di leher, pergelangan tangan, pergelangan kaki, hingga bokong.\n  - Terjadinya penebalan kulit yang akhirnya berkembang menjadi gatal permanen.\nAnak yang mengalami masalah ini sebelum usianya lima tahun memiliki kemungkinan tidak menunjukkan gejalanya lagi saat memasuki masa remaja.\n\nGejala eksim pada orang dewasa :\nSaat masalah ini terjadi pada orang dewasa, berikut beberapa gejala yang ditimbulkan :\n  - Ruam dengan sisik yang lebih parah.\n  - Ruam timbul pada lipatan siku atau lutut.\n  - Ruam dapat menutupi sebagian besar tubuh.\n  - Kulit yang sangat kering pada area yang terserang.\n  - Ruam yang gatal secara permanen.\n  - Mengalami infeksi kulit.\nTampilan kulit yang terserang gangguan ini tergantung dari seberapa sering digaruk dan terjadinya infeksi pada kulit. Menggaruk dan menggosok lebih sering dapat menimbulkan iritasi, peradangan, dan membuat rasa gatal lebih parah.\n\nPenyebab Eksim : \nEksim dapat disebabkan oleh faktor dari luar (eksogen), seperti bahan kimia, mikroorganisme (bakteri, jamur). Selain itu, masalah ini juga bisa disebabkan oleh pengaruh dari dalam (endogen), seperti eksim atopik. Sebagian lainnya belum diketahui secara pasti, terutama yang berhubungan dengan endogen.\n\nFaktor Risiko Eksim :\nDipercaya jika gangguan ini berkembang dari kombinasi antara faktor genetik dan lingkungan. Selain itu, anak-anak lebih rentan untuk mengalami masalah ini dibandingkan orang yang lebih tua. Anak yang kedua orang tuanya memiliki kondisi ini, risikonya untuk mengalami hal yang sama lebih tinggi.\nBeberapa faktor lingkungan yang dapat meningkatkan risiko terjadinya eksim adalah:\n  - Iritan: Segala hal yang dapat menyebabkan iritasi, termasuk sabun, deterjen, sampo, desinfektan, dan lain-lain.\n  - Alergen: Tungau debu, hewan peliharaan, serbuk sari, dan segala hal yang dapat menyebabkan eksim, atau disebut juga eksim alergi.\n  - Mikroba: Eksim juga bisa disebabkan oleh bakteri seperti Staphylococcus aureus, virus, dan jamur tertentu.\n  - Suhu panas dan dingin: Cuaca yang sangat panas dan sangat dingin, kelembapan tinggi dan rendah, dan keringat akibat olahraga juga dapat menyebabkan eksim.\n  - Makanan: Produk susu, telur, kacang-kacangan dan biji-bijian, produk kedelai, dan gandum dapat menyebabkan gangguan kulit ini pada beberapa orang.\n  - Stres: Hal ini bukanlah penyebab langsung dari eksim, tetapi dapat memperburuk gejalanya.\n  - Hormon: Wanita mungkin mengalami peningkatan gejala eksim ketika kadar hormonnya berubah, seperti selama kehamilan dan pada titik-titik tertentu dalam siklus menstruasi.\n\nDiagnosis Eksim : \nEksim dapat didiagnosis dengan cara melakukan pemeriksaan kulit dan riwayat kesehatan. Dokter juga bisa melakukan pemeriksaan menggunakan tes patch. Tes ini dilakukan untuk melihat adanya potensi alergi. Selain itu, dokter juga dapat melakukan pemeriksaan untuk mendeteksi kondisi yang dapat memicu terjadinya gangguan pada kulit ini.\n\nPengobatan Eksim\nDipercaya jika belum ada obat yang dapat mengatasi eksim. Perawatan terhadap kondisi ini bertujuan untuk menyembuhkan kulit yang terserang serta mencegah gejalanya. Pengobatan yang dapat dilakukan berdasarkan berbagai faktor. Nah, berikut beberapa cara pengobatan yang bisa dilakukan :\nAda beberapa perawatan rumahan yang bisa dilakukan untuk mengatasi eksim, yaitu: \n- Mandi dengan air hangat. \n- Mengoleskan pelembap setelah mandi. \n- Menggunakan pelembap setiap hari. \n- Memakai katun dan kain lembut. \n- Menghindari bahan pakaian yang kasar, gatal, serta pakaian yang ketat. \n- Menggunakan pelembap udara dalam cuaca yang kering atau dingin. \n- Menghindari pemicu terjadinya eksim. \n\nPengobatan medis :\nSelain pengobatan rumahan, ada juga beberapa pengobatan medis yang bisa dilakukan, seperti :\n- Penggunaan antihistamin. Metode ini dapat meredakan eksim yang diinduksikan oleh alergi. Namun, perlu diperhatikan jika obat ini dapat menyebabkan kantuk jika dikonsumsi secara oral. Dokter kerap menyarankan untuk menggunakan obat secara topikal.\n- Penggunaan kortikosteroid oles. Obat ini dapat digunakan untuk menekan peradangan akibat eksim. Namun, pengobatan seperti steroid sebaiknya hanya digunakan di daerah yang mengalami peradangan dan tidak untuk area lain, terutama area luka dan wajah.\n- Penggunaan pelembap kulit. Pilih pelembap yang benar-benar sesuai dengan kondisi kulit. Cobalah lebih sering mengoleskannya untuk menghindari masalah kulit yang lebih meluas.\n\nPencegahan Eksim :\nPencegahan pada eksim umumnya dilakukan dengan melakukan perawatan kulit yang benar. Pastikan untuk menghindari kulit yang terlalu kering atau terlalu basah. Jaga kelembapan kulit serta hindari keringat yang berlebih. Pastikan juga hindari kontak dengan berbagai pemicu dari gangguan ini. Beberapa cara mencegahnya adalah:\n- Hindari menggunakan bahan yang menimbulkan rasa gatal, seperti wol.\n- Jangan gunakan sabun dan deterjen dengan kandungan yang keras.\n- Pastikan untuk menggunakan pelembap udara di kamar tidur.\n- Kurangi pikiran yang menyebabkan stres.\n- Sebaiknya hindari untuk mengonsumsi makanan pemicu alergi dan pemicu iritasi.\n- Cegah perubahan suhu dan kelembaban kulit yang ekstrim.\n- Hindari mandi menggunakan air yang terlalu panas.\n- Jangan memanaskan dan mendinginkan kulit secara berlebih.\n- Gunakan pelindung ketika bersentuhan dengan deterjen atau bahan kimia lainnya.\nUntuk bayi, pastikan untuk memberikan ASI eksklusif selama tiga bulan pertama atau bahkan hingga satu tahun. Bayi juga harus dilindungi berbagai alergen yang bisa menyebabkan eksim, seperti bulu hewan, tungau, serta jamur.\n\nKapan Harus ke Dokter?\nAda beberapa kondisi yang dapat menjadi tanda seseorang terserang eksim dan perlu segera menghubungi dokter, seperti :\n- Terlihat tanda-tanda mengalami infeksi, seperti demam, kemerahan, kehangatan, nanah, atau lecet.\n- Eksim pada kulit tiba-tiba berubah atau memburuk.\n- Perawatan yang dilakukan tidak kunjung berhasil.\n- Kehilangan waktu tidur atau aktivitas harian yang terganggu.\n- Kulit terasa sakit.'
]

solusi_penyakit_dermatitis = [
    'Pengobatan\n\n1. Mengompres dingin\nKompres dingin bertujuan untuk meredakan gatal tanpa menggaruknya. Bungkuslah beberapa buah es dengan handuk, lalu tempelkan ke kulit selama 20 menit sebanyak 3-4 kali sehari.\n\n2. Mandi air hangat\nMandi air hangat juga membantu meredakan gatal-gatal yang mengganggu. Namun, jangan mandi terlalu lama atau dengan air yang terlalu panas karena hal ini justru membuat kulit makin kering sehingga memperparah gejala.\n\n3. Jangan menggaruk kulit\nAgar kondisi kulit tidak bertambah parah, jangan menggaruk terlalu keras bagian kulit Anda yang terkena dermatitis. Sebagai gantinya, cobalah menepuk-nepuk, mencubit lembut, atau menggunakan kompres untuk meredakan gatal.\n\n4. Gunakan pakaian berbahan katun\nPakaian berbahan katun membantu mencegah iritasi akibat eksim. Selain menyerap keringat, bahan ini juga aman dan lembut di kulit sehingga tidak akan melukai area yang terkena dermatitis.\n\n5. Lakukan kegiatan menyenangkan\nStres adalah salah satu hal yang memperparah gejala dermatitis. Anda bisa mencoba menghalaunya dengan kegiatan menyenangkan seperti yoga, melakukan hobi baru, mendengarkan musik, atau sekadar menarik napas dalam-dalam agar tubuh rileks.\n\n6. Mengoleskan tea tree oil\nTea tree oil mengandung zat antijamur, dan antiradang sehingga membantu mengatasi dermatitis seboroik. Cukup campurkan beberapa tetes tea tree oil dengan minyak kelapa atau zaitun, lalu oleskan ke kulit kepala Anda secara rutin.\n\n7. Menggunakan aloe vera\nLidah buaya termasuk tanaman dengan kandungan antiradang yang tinggi. Sebuah studi yang diterbitkan dalam Indian Journal of Dermatology bahkan menyebutkan bahwa ekstrak tanaman ini bisa meringankan gejala dermatitis seboroik.\n\n8. Minum suplemen minyak ikan\nSuplemen minyak ikan membantu menekan gejala dermatitis yang dipicu oleh alergi. Selain itu, suplemen yang satu ini juga membantu menjaga kesehatan tubuh secara keseluruhan karena mengandung asam lemak omega 3.\n\nDan jika Pengobatan rumahan ini tidak berhasil anda harus konsultasi ke dokter spesialis kulit di rumah sakit yang ada di sekitar tempat tinggal anda.'
]

info_penyakit_dermatitis = [
    '  Penyakit kulit dermatitis adalah penyakit kulit yang disebabkan oleh peradangan akibat kontak langsung dengan zat iritan (mudah mengiritasi kulit) atau alergen (pemicu alergi) di lingkungan sekitar. Masalah kulit ini juga dapat dipengaruhi oleh faktor genetik.\nGejala utamanya adalah ruam bengkak kemerahan yang tampak sangat kering dan terasa gatal. Kulit yang terdampak biasanya terasa nyeri ketika disentuh serta dipenuhi lepuhan kecil yang dapat mengelupas mengeluarkan cairan.\nDermatitis bukan penyakit kulit menular. Meski begitu, gejalanya perlu dikenali sejak dini. Penyakit ini bisa dikendalikan dengan baik melalui kombinasi pengobatan dan pencegahan kontak terhadap hal-hal yang memicu peradangan kulit.\n\nSeberapa umumkah kondisi ini?\n  Dermatitis merupakan penyakit peradangan kulit yang sangat umum. Penyakit ini biasanya menyerang 15– 20% anak-anak dan 1 – 3% dari orang dewasa di seluruh dunia. Orang dengan riwayat alergi dan asma lebih rentan mengalaminya.\n\nTanda-tanda dan gejala\nApa saja tanda dan gejala dermatitis?\nPenyakit kulit ini terdiri dari beberapa jenis. Tanda-tanda dan gejalanya sangat tergantung pada jenis yang Anda miliki. Dari sekian banyak yang ada, tiga macam dermatitis yang paling umum dan perlu dikenali adalah:\n  - Dermatitis atopik (eksim).\n  - Dermatitis kontak (kontak iritan atau kontak alergi).\n  - Dermatitis seboroik.\nSetiap jenis dermatitis memiliki gejala dan penyebab yang berbeda. Ada yang muncul dalam waktu lama dan ada yang hanya muncul sementara jika terpapar zat tertentu.\n\nKapan saya harus periksa ke dokter?\nApabila Anda atau keluarga Anda terkena penyakit kulit ini, segeralah berkonsultasi ke dokter saat:\n  - Merasa sangat tidak nyaman sehingga sulit tidur dan aktivitas lain menjadi terhambat.\n  - Kulit terasa sangat sakit.\n  - Curiga kulit mengalami infeksi misalnya keluarnya nanah dari luka di kulit.\n  - Telah mencoba melakukan berbagai perawatan rumahan tetapi tak kunjung membaik.\nDiagnosis dan perawatan dini dapat mencegah penyakit bertambah parah serta mengurangi risiko munculnya kondisi medis darurat lain. Ini sebabnya Anda dianjurkan untuk memeriksakan diri ke dokter saat berbagai gejalanya telah muncul.\nKemungkinan ada gejala lain yang belum disebutkan di atas. Jika Anda memiliki pertanyaan lainnya, jangan sungkan untuk bertanya ke dokter. Diskusikan dengan dokter mengenai perawatan dan pengobatan apa yang paling tepat untuk Anda.\n\nPenyebab\nApa penyebab dermatitis?\n1. Dermatitis atopik (eksim)\nJenis penyakit kulit ini kemungkinan disebabkan oleh berbagai faktor, seperti:\n  - kulit kering.\n  - perbedaan kondisi genetik.\n  - kesalahan pada sistem imun.\n  - bakteri pada kulit.\n  - faktor lingkungan.\n  - adanya riwayat eksim dalam keluarga.\n  - adanya riwayat alergi atau asma.\n\n2. Dermatitis kontak\nPenyakit ini terbagi menjadi dermatitis alergi kontak dan dermatitis iritan kontak. Dermatitis kontak alergi disebabkan karena sentuhan langsung dengan pemicu alergi, sedangkan dermatitis kontak iritan terjadi akibat kontak dengan zat penyebab iritasi.\nBeberapa alergen dan iritan yang sering menjadi penyebabnya yakni:\n  - tanaman poison ivy atau tanaman beracun yang berasal dari tanaman obat, bunga, buah-buahan, dan sayuran.\n  - perhiasan dengan nikel.\n  - zat kimia dalam produk pembersih.\n  - parfum.\n  - kosmetik.\n  - zat pengawet pada krim dan losion.\n\n3. Dermatitis seboroik\nPeradangan kronis pada kulit kepala umumnya disebabkan oleh pertumbuhan jamur Malassezia pada kelenjar minyak yang tersebar di kulit. Sistem imun kemungkinan bereaksi secara tidak wajar terhadap jamur tersebut sehingga jamur dan minyak berkembang tanpa terkendali.\n\nFaktor-faktor risiko\nSiapa yang lebih berisiko terkena dermatitis?\nAda banyak faktor yang meningkatkan risiko Anda terkena peradangan kulit, di antaranya adalah sebagai berikut.\n1. Usia\nPenyakit kulit ini dapat muncul pada usia berapa pun, tapi dermatitis atopik (eksim) lebih banyak dijumpai pada bayi. Oleh sebab itu, bayi dan anak-anak lebih berisiko terkena eksim.\n\n2. Menderita alergi dan asma\nOrang yang menderita asma dan alergi lebih berisiko terkena dermatitis atopik. Namun, tidak diketahui hubungan pasti antara alergi dan asma dengan dermatitis atopik.\n\n3. Sering terkena alergen di tempat kerja\nPekerjaan yang membuat Anda terpapar langsung dengan logam, pelarut, atau produk pembersih tertentu meningkatkan risiko dermatitis kontak. Orang yang bekerja dalam bidang kesehatan juga rentan terkena eksim, terutama pada tangan.\n\n4. Menderita penyakit tertentu\nAnda berisiko lebih tinggi terkena peradangan kronis pada kulit kepala bila menderita penyakit gagal jantung kongestif, penyakit Parkinson, dan HIV.\n\n5. Riwayat keluarga\nDermatitis adalah salah satu penyakit kulit yang diturunkan dari orangtua ke anak. Maka dari itu, seseorang yang lahir dari keluarga dengan riwayat penyakit ini biasanya lebih rentan terkena penyakit yang sama.\n\n6. Terlalu sering mencuci tangan\nKebiasaan tertentu ternyata bisa meningkatkan risiko seseorang terkena peradangan kronis, contohnya terlalu sering mencuci dan mengeringkan tangan. Pasalnya, kebiasaan ini bisa menghilangkan minyak alami kulit dan mengubah keseimbangan pH-nya.\n\nPencegahan\nBagaimana cara mencegah dermatitis kambuh?\nAnda bisa mencegah kambuhnya penyakit ini dengan menjaga kulit tetap lembap dan terawat. Berikut kiat-kiatnya.\n  - Membatasi waktu mandi hanya selama 5-10 menit.\n  - Menggunakan sabun yang tidak menghasilkan banyak busa.\n  - Mengeringkan tubuh dengan handuk yang halus.\n  - Menggunakan minyak atau krim pelembap kulit.\n  - Menghindari zat penyebab alergi atau iritasi.\n  - Memakai sarung tangan bila hendak menggunakan produk pembersih.\n\nDermatitis merupakan penyakit peradangan pada kulit dengan pemicu yang beragam. Beberapa di antaranya disebabkan oleh alergi, dan ada pula yang terjadi karena kontak langsung dengan zat pemicu iritasi.Kenali apa pemicu kondisi Anda dan diskusikan bersama dokter untuk mendapatkan perawatan yang sesuai. \nPerawatan dini amat membantu dalam mengatasi gejala dan mencegah penyakit bertambah parah.'
]


solusi_penyakit_impetigo = [
    'Pengobatan Impetigo :\nSalep atau krim antibiotik, seperti mupirocin atau polymyxin B, digunakan jika infeksi yang terjadi tergolong ringan, hanya menyerang satu area tubuh, dan belum menyebar terlalu luas. Sebelum mengoleskan krim atau krim antIbiotik, dianjurkan untuk merendam luka dengan air hangat atau mengompres hangat untuk melunakkan koreng.\nJika impetigo bertambah parah dan mulai menyebar ke bagian tubuh lainnya, dokter akan memberikan antibiotik dalam bentuk tablet, seperti clindamycin atau antibiotik golongan sefalosporin.\nTablet antibiotik juga diberikan jika krim atau salep tidak lagi efektif mengobati impetigo. Penting untuk diingat, jangan menghentikan konsumsi obat tanpa seizin dokter meskipun gejalanya sudah membaik, agar infeksi tidak kambuh.'
]

info_penyakit_impetigo =[
    '   Impetigo adalah infeksi kulit menular yang banyak dialami oleh bayi dan anak-anak. Infeksi ini ditandai dengan kemunculan bercak merah dan lepuhan di kulit, terutama di wajah, tangan, dan kaki.\nImpetigo bukan kondisi yang serius, tetapi penyebaran penyakit ini sangat mudah terjadi. Infeksi dapat terjadi pada kulit yang sehat (impetigo primer) atau akibat kondisi lain (impetigo sekunder), seperti eksim atopik.\n\nPenyebab Impetigo\nPenyebab utama impetigo adalah infeksi bakteri. Bakteri dapat menular melalui kontak langsung dengan penderita atau melalui perantara berupa barang yang sebelumnya digunakan oleh penderita, seperti baju atau handuk.\nInfeksi lebih mudah menular jika ada luka terbuka, seperti luka goresan, gigitan serangga, atau cedera akibat terjatuh. Luka tersebut menyebabkan bakteri lebih mudah masuk ke dalam tubuh. Impetigo juga dapat muncul akibat kelainan kulit lainnya, seperti eksim atopik atau kudis.\nImpetigo dapat dialami oleh siapa saja, tetapi lebih sering terjadi pada anak-anak usia 2–5 tahun. Hal ini dikarenakan sistem kekebalan tubuh mereka belum cukup kuat untuk melawan bakteri penyebab infeksi.\n\nAda beberapa faktor lain yang dapat meningkatkan risiko seseorang terkena impetigo, yaitu:\n  - Menderita diabetes.\n  - Memiliki daya tahan tubuh lemah, misalnya karena menderita HIV/AIDS.\n  - Melakukan olahraga yang menyebabkan kontak antarkulit dengan orang lain, seperti gulat atau sepak bola.\n  - Bertempat tinggal di lingkungan yang padat penduduk.\n\nGejala Impetigo\nGejala impetigo tidak langsung muncul setelah penderita terinfeksi. Gejala biasanya baru terlihat 4–10 hari setelah penderita pertama kali terpapar bakteri. Keluhan yang muncul pun bervariasi, tergantung pada jenis impetigo yang dialami.Berikut ini adalah gejala impetigo berdasarkan jenisnya :\n1. Impetigo krustosa\nImpetigo krustosa merupakan jenis impetigo yang paling sering dialami oleh anak-anak dan lebih mudah menular. Gejala impetigo krustosa meliputi:\n  - Bercak kemerahan yang terasa gatal di sekitar mulut dan hidung, tetapi tidak menimbulkan nyeri.\n  - Luka pada bercak akibat digaruk.\n  - Iritasi pada kulit di sekitar luka.\n  - Koreng berwarna kuning kecokelatan di sekitar luka.\n  - Bekas kemerahan di kulit akibat koreng yang dapat hilang dalam jangka waktu beberapa hari atau minggu.\n\nImpetigo bulosa\nImpetigo bulosa merupakan jenis impetigo yang lebih serius. Gejalanya berupa :\n  - Lepuhan berisi cairan bening di bagian tubuh antara leher dan pinggang, serta lengan dan tungkai.\n  - Nyeri di area lepuhan dan gatal pada kulit di sekitarnya.\n  - Lepuhan pecah, menyebar, dan menimbulkan koreng berwarna kekuningan, tetapi akan menghilang setelah beberapa hari.\nTerkadang, impetigo bulosa juga disertai dengan demam dan kemunculan benjolan di sekitar leher akibat pembengkakan kelenjar getah bening.\n\nKapan harus ke dokter\nSegera periksakan ke dokter kulit jika mengalami gejala impetigo seperti yang telah disebutkan di atas. Anda harus lebih waspada apabila gejala tersebut terjadi selama lebih dari seminggu.\nImpetigo harus secepatnya ditangani, karena deteksi dan penanganan sejak dini dapat menghambat atau menghentikan penyebaran infeksi, serta mempercepat proses penyembuhan.\n\nDiagnosis Impetigo\nPada pemeriksaan awal, dokter akan menanyakan gejala dan memeriksa kondisi pada kulit yang terinfeksi, seperti lepuhan atau koreng.\nDokter juga dapat melakukan pemeriksaan terhadap sampel cairan dari luka di kulit. Tujuannya adalah untuk mendeteksi jenis bakteri yang menyebabkan impetigo dan menentukan pengobatan yang tepat.\nJika diperlukan, dokter akan melakukan pengambilan dan pemeriksaan terhadap sampel jaringan kulit di laboratorium. Pemeriksaan ini dilakukan bila dicurigai gejala disebabkan oleh kondisi lain.\n\nPencegahan Impetigo\nImpetigo merupakan penyakit yang menular. Oleh sebab itu, cara terbaik untuk mencegah penularannya adalah dengan menjaga kebersihan dan lingkungan. Beberapa upaya yang dapat dilakukan adalah :\n  - Rajin mencuci tangan, terutama setelah beraktivitas di luar.\n  - Menutup luka agar bakteri tidak masuk ke dalam tubuh.\n  - Memotong dan selalu menjaga kebersihan kuku.\n  - Tidak menyentuh atau menggaruk luka untuk menurunkan risiko penyebaran infeksi.\n  - Mencuci pakaian atau membersihkan benda yang telah digunakan, untuk membunuh bakteri.\n  - Menghindari berbagi penggunaan peralatan makan, handuk, atau pakaian dengan penderita impetigo.\n  - Mengganti sprei, handuk, atau pakaian yang digunakan penderita setiap hari, sampai luka tidak lagi menularkan infeksi.\n\nAnak yang menderita impetigo sangat dianjurkan untuk tidak keluar rumah sampai gejala yang dialaminya reda. Tindakan ini dilakukan untuk mengurangi interaksi dengan anak lain yang dapat meningkatkan risiko penularan.'
]


solusi_penyakit_jerawat = [
    'Pengobatan dan Pencegahan Jerawat\n\nPengobatan jerawat disesuaikan dengan tingkat keparahan kondisinya. Pengobatan jerawat terbagi menjadi dua, yaitu pemberian obat untuk mengatasi atau menghilangkan jerawat, dan terapi estetika untuk membantu pengobatan jerawat serta memperbaiki penampilan kulit.\nObat jerawat dapat berupa obat oles mengandung tretinoin atau benzoyl peroxide, isotretinoin, obat antibiotik minum, serta terapi hormon.\nSementara terapi estetika untuk jerawat dapat berupa chemical peeling, terapi laser, dan pengangkatan komedo. Terapi laser dan mikrodermabrasi juga dapat dilakukan untuk mengatasi bekas jerawat.\nCara mencegah jerawat adalah rutin membersihkan wajah, tubuh, dan rambut menggunakan sabun pembersih wajah, sabun mandi, atau sampo yang sesuai dengan tipe kulit atau rambut. Jerawat juga dapat dicegah dengan menggunakan produk skincare dan kosmetik yang noncomedogenic, menerapkan pola makan sehat, serta mengelola stres dengan baik.'
]

info_penyakit_jerawat = [
    '   Jerawat adalah masalah kulit yang terjadi ketika pori-pori kulit, tepatnya folikel rambut, tersumbat oleh kotoran, debu, minyak, atau sel kulit mati. Akibatnya, terjadi peradangan pada pori-pori tersebut dan bisa juga disertai infeksi. Jerawat sering muncul di wajah, leher, punggung, atau dada.\nJerawat disebut juga acne vulgaris. Masalah kulit ini dapat dialami oleh siapa saja, tetapi umumnya pertama kali muncul di masa pubertas, yaitu usia 10–18 tahun. Kondisi jerawat cenderung lebih parah pada remaja laki-laki dan orang yang memiliki tipe kulit berminyak.\nJerawat merupakan masalah kulit yang sangat umum, terutama pada orang yang berusia 11–30 tahun. Bahkan, hampir setiap orang pernah mengalami jerawat.\n\nPenyebab dan Gejala Jerawat :\nJerawat disebabkan oleh penyumbatan di pori-pori kulit, tepatnya di akar rambut (folikel rambut). Pada folikel rambut, terdapat kelenjar minyak (kelenjar sebasea) yang normalnya memproduksi minyak (sebum) untuk menjaga kelembapan dan melindungi kulit.\nJerawat timbul jika saluran keluar minyak tersebut tersumbat akibat produksi minyak yang berlebihan, penumpukan sel-sel kulit mati, atau infeksi bakteri.\nJerawat muncul berupa bintik komedo atau benjolan pada area kulit yang banyak memiliki folikel rambut, seperti wajah, leher, bahu, dada, dan punggung. Bentuk dan ukuran jerawat tergantung pada tingkat keparahannya, mulai dari komedo hitam atau komedo putih, benjolan kecil kemerahan (papula dan pustula), hingga benjolan besar berisi nanah (kista).\nKomedo biasanya tidak terasa nyeri. Sebaliknya, jerawat berupa benjolan besar bisa terasa nyeri ketika disentuh.\n\nPengobatan dan Pencegahan Jerawat :\nPengobatan jerawat disesuaikan dengan tingkat keparahan kondisinya. Pengobatan jerawat terbagi menjadi dua, yaitu pemberian obat untuk mengatasi atau menghilangkan jerawat, dan terapi estetika untuk membantu pengobatan jerawat serta memperbaiki penampilan kulit.\nObat jerawat dapat berupa obat oles mengandung tretinoin atau benzoyl peroxide, isotretinoin, obat antibiotik minum, serta terapi hormon.\nSementara terapi estetika untuk jerawat dapat berupa chemical peeling, terapi laser, dan pengangkatan komedo. Terapi laser dan mikrodermabrasi juga dapat dilakukan untuk mengatasi bekas jerawat.\nCara mencegah jerawat adalah rutin membersihkan wajah, tubuh, dan rambut menggunakan sabun pembersih wajah, sabun mandi, atau sampo yang sesuai dengan tipe kulit atau rambut. Jerawat juga dapat dicegah dengan menggunakan produk skincare dan kosmetik yang noncomedogenic, menerapkan pola makan sehat, serta mengelola stres dengan baik.'
]


solusi_penyakit_kudis = [
    'Pengobatan Kudis\nDianjurkan untuk melakukan pemeriksaan ke dokter.\n\n Penanganan scabies bertujuan untuk membasmi tungau, meredakan gatal dan peradangan, serta mengatasi infeksi sekunder, seperti dijelaskan di bawah ini :\n\nMembasmi tungau\nUntuk membasmi tungau dan telurnya, dokter akan meresepkan obat scabies yang biasa dioleskan saat malam hari. Obat oles yang diresepkan dokter antara lain:\n  - Krim permethrin 5%.\n  - Krim krotamiton 10%.\n  - Losion benzil benzoate 25%.\n  - Sulfur presipitatum (5–10%).\n  - Losion indane (1%).'
]

info_penyakit_kudis = [
    '   Kudis adalah kondisi yang ditandai dengan gatal di kulit, terutama di malam hari. Gatal ini disertai dengan kemunculan ruam berbintik yang menyerupai jerawat atau lepuhan kecil bersisik. Kondisi ini terjadi akibat tungau yang hidup dan bersarang di kulit.\nKudis atau scabies merupakan penyakit yang mudah menular, baik melalui kontak langsung maupun tidak langsung. Penyakit ini sangat mudah menyebar, terutama jika ada kontak dekat antarmanusia di suatu lingkungan.\nDi Indonesia, kudis banyak ditemukan di wilayah padat penduduk, area kumuh, dan pondok pesantren. Karena mudah menular, penanganan scabies perlu dilakukan secara menyeluruh pada kelompok yang terpapar penyakit ini.\n\nPenyebab Kudis\n   Kudis disebabkan oleh tungau Sarcoptes scabiei. Tungau ini mengeluarkan air liur, telur, dan kotoran. Hal tersebut memicu respons dari sistem kekebalan tubuh sehingga menimbulkan gatal.\n   Siklus perkembangan parasit tungau dimulai ketika tungau betina masuk ke kulit manusia, kemudian membuat lubang yang menyerupai terowongan untuk dijadikan sarang. Selanjutnya, tungau jantan akan memasuki sarang tersebut untuk kawin dengan tungau betina.\n   Setelah kawin, tungau jantan akan mati dan tungau betina akan mulai bertelur di sarang tersebut. Telur akan menetas 3–4 hari setelahnya. Setelah menetas, tungau muda akan keluar ke permukaan kulit selama 1–2 minggu ke depan sampai mereka tumbuh menjadi tungau dewasa.\n   Setelah dewasa, tungau jantan akan menetap di permukaan kulit. Sementara tungau betina akan masuk lagi ke dalam kulit untuk membuat sarang baru dan mengulang siklus yang sama.\n   Perlu diketahui, tungau kudis adalah parasit yang tinggal di lapisan kulit yang dalam. Hal ini membuatnya kebal terhadap sabun dan air panas, serta tidak akan hilang jika kulit hanya digosok-gosokkan. Tanpa penanganan yang tepat, tungau akan terus berkembang biak dan siklus perkembangan tungau akan terus berlanjut.\nTungau Sarcoptes scabiei tidak bisa terbang atau melompat sehingga penularannya hanya dapat terjadi melalui dua cara, yakni :\n\nKontak langsung :\nTungau dapat menular dengan mudah melalui kontak langsung dengan penderita kudis, seperti pegangan tangan dalam waktu yang lama atau hubungan seksual. Namun, kontak fisik yang singkat, seperti berjabat tangan atau berpelukan, hanya berpotensi kecil menularkan tungau.\n\nKontak tidak langsung :\nMeski jarang, tungau juga bisa menular melalui kontak tidak langsung, misalnya ketika berbagi penggunaan pakaian, handuk, atau tempat tidur dengan penderita kudis. Hal ini dapat terjadi karena tungau bisa menetap selama 2–3 hari di benda tertentu.Scabies juga dapat menyerang hewan, seperti anjing dan kucing. Namun, parasit kudis dari hewan tidak dapat menular ke manusia karena perbedaan jenis tungau antara keduanya. Tungau dari hewan tidak bisa berkembang di kulit manusia dan hanya akan menimbulkan gejala ringan di kulit.\nSemua orang dapat tertular kudis. Namun, ada beberapa kelompok yang memiliki risiko tinggi untuk tertular penyakit ini, yaitu :\n  - Orang yang tinggal di lingkungan padat penduduk.\n  - Bayi dan anak-anak.\n  - Orang lanjut usia, terutama yang tinggal di panti jompo.\n  - Orang dewasa yang aktif secara seksual.\n  - Seseorang yang tengah menjalani rawat inap.\n  - Petugas kesehatan yang merawat pasien dengan kudis.\n  - Seseorang yang memiliki daya tahan tubuh lemah, seperti penderita HIV/AIDS atau kanker.\n\nKapan harus ke dokter :\nLakukan pemeriksaan ke dokter jika Anda mengalami keluhan di kulit yang diduga sebagai tanda penyakit kudis. Selain kudis, keluhan tersebut juga bisa disebabkan oleh kondisi kulit lain. Maka dari itu, dokter akan membantu menemukan penyebab pasti sekaligus menentukan penanganan yang tepat untuk Anda.Jika Anda telah melakukan kontak erat dengan penderita scabies, periksakan diri ke dokter meski belum ada gejala yang muncul di kulit. Pemeriksaan dan penanganan lebih awal dapat membantu meredakan gejala yang mungkin muncul di kemudian hari.'
]


solusi_penyakit_kurap = [
    'Pengobatan dan Pencegahan Kurap\n\nKurap dapat diatasi dengan salep kurap atau antijamur, seperti clotrimazole atau miconazole. Jika kurap tidak juga membaik atau sembuh setelah 2 minggu diobati, segera konsultasikan ke dokter. Dokter akan memberikan obat lain yang lebih kuat.\nKurap dapat dicegah dengan menjaga kebersihan. Di samping itu, hindari berbagi pemakaian barang pribadi dengan orang lain, serta mandi, cuci rambut, dan ganti baju setiap hari atau segera setelah berkeringat.'
]

info_penyakit_kurap = [
    '   Kurap adalah infeksi jamur pada kulit yang menimbulkan ruam melingkar berwarna merah. Kurap dapat terjadi di beberapa area tubuh, seperti kepala, wajah, tangan, kaki, atau selangkangan.Jamur merupakan organisme yang bisa hidup di berbagai tempat, termasuk di tubuh manusia. Sebagian jamur tidak berbahaya bagi manusia, tetapi sebagian lainnya dapat berbahaya jika tumbuh dan berkembang di tubuh manusia dengan cepat.Karena bentuknya seperti cincin atau cacing yang melingkar, kurap juga dikenal dengan sebutan ringworm.\n\nPenyebab dan Gejala Kurap :\nKurap disebabkan oleh infeksi jamur pada kulit. Jamur ini dapat menular melalui kontak langsung dengan penderita atau kontak tidak langsung dengan benda atau tanah yang terkontaminasi.Udara panas dan lembap, berbagi pemakaian barang pribadi, dan memakai pakaian yang ketat bisa membuat seseorang lebih rentan terkena kurap.Kurap ditandai dengan munculnya ruam bersisik berwarna kemerahan di permukaan kulit. Ruam kulit ini dapat meluas. Meski demikian, gejala kurap dapat berbeda-beda pada tiap orang, tergantung pada lokasi kurap.\n\nPengobatan dan Pencegahan Kurap :\nKurap dapat diatasi dengan salep kurap atau antijamur, seperti clotrimazole atau miconazole. Jika kurap tidak juga membaik atau sembuh setelah 2 minggu diobati, segera konsultasikan ke dokter. Dokter akan memberikan obat lain yang lebih kuat.\nKurap dapat dicegah dengan menjaga kebersihan. Di samping itu, hindari berbagi pemakaian barang pribadi dengan orang lain, serta mandi, cuci rambut, dan ganti baju setiap hari atau segera setelah berkeringat.'
]

solusi_penyakit_panu = [
    'Pengobatan dan Pencegahan Panu\n\nPengobatan panu adalah dengan pemberian obat antijamur. Namun, sebelum menggunakan obat antijamur, disarankan untuk berkonsultasi terlebih dahulu dengan dokter.\nCara untuk mencegah panu adalah dengan menurunkan risiko terjadinya penyakit ini, antara lain dengan menghindari paparan sinar matahari yang terlalu lama, serta menjaga kebersihan dan kesehatan kulit.'
]

info_penyakit_panu = [
    '   Panu adalah infeksi jamur pada kulit yang disebabkan oleh golongan jamur Malassezia. Infeksi jamur ini menyebabkan gangguan pada pigmen kulit sehingga menimbulkan bercak yang berwarna lebih terang atau lebih gelap di permukaan kulit.Panu, yang juga dikenal dengan pityriasis versicolor atau tinea versicolor, bukanlah penyakit menular. Panu muncul secara perlahan, kemudian seiring waktu menyatu dan membentuk bercak kulit yang lebih besar.Area kulit yang paling sering terkena panu adalah punggung, dada, lengan atas, leher, dan perut.\n\nPenyebab dan Gejala Panu :\nPanu disebabkan oleh jamur Malassezia yang tumbuh dan berkembang dengan cepat di kulit. Belum diketahui apa yang menyebabkan kondisi tersebut, tetapi diduga terkait dengan beberapa faktor, di antaranya perubahan hormon dan kulit berminyak.Gejala utama panu adalah bercak di kulit yang berwarna lebih terang atau lebih gelap. Bercak tersebut juga dapat disertai dengan gejala lain, seperti gatal, serta kulit kering atau bersisik di area yang terinfeksi.\n\nPengobatan dan Pencegahan Panu :\nPengobatan panu adalah dengan pemberian obat antijamur. Namun, sebelum menggunakan obat antijamur, disarankan untuk berkonsultasi terlebih dahulu dengan dokter.\nCara untuk mencegah panu adalah dengan menurunkan risiko terjadinya penyakit ini, antara lain dengan menghindari paparan sinar matahari yang terlalu lama, serta menjaga kebersihan dan kesehatan kulit.'
]

solusi_penyakit_lichen_planus = [
    'Dianjurkan untuk melakukan pemeriksaan ke dokter. \n\nPengobatan Lichen Planus :\nPengobatan lichen planus bertujuan untuk meredakan gejala, mencegah munculnya komplikasi, dan menurunkan risiko terjadinya kekambuhan penyakit ini di kemudian hari. Metode pengobatannya akan disesuaikan dengan kesehatan pasien dan tingkat keparahan kondisinya secara menyeluruh.Lichen planus ringan biasanya dapat sembuh dengan sendirinya dalam beberapa minggu atau beberapa bulan. Namun, jika pasien mengalami lichen planus yang parah, dokter akan memberikan obat untuk membantu meringankan gejala yang dialami pasien.\n\nBeberapa metode pengobatan yang dapat dilakukan oleh dokter untuk menangani lichen planus adalah :\n- Pemberian obat antihistamin, dalam bentuk obat minum (oral) atau oles, untuk mengurangi gatal yang diakibatkan lichen planus.\n- Pemberian obat kortikosteroid, dalam bentuk salep, tablet, atau injeksi, untuk mengurangi peradangan.\n- Pemberian obat imunosupresan, dalam bentuk krim atau salep, untuk menekan aktivitas sistem imun yang berlebihan sehingga gejala mereda.\n- Penanganan dengan fototerapi atau sinar ultraviolet, untuk menghilangkan lichen planus di kulit.\nJika lichen planus tidak juga membaik dengan obat-obatan dan fototerapi, dokter dapat memberikan salep retinoid. Namun, perlu diketahui bahwa salep retinoid bisa menyebabkan kulit mengalami iritasi, kemerahan, dan mengelupas. Salep retinoid juga berisiko menyebabkan cacat janin jika dikonsumsi oleh ibu hamil.Untuk menangani lichen planus yang sudah disertai komplikasi, dokter akan memberikan obat antibiotik atau antijamur.\n\nSelain pengobatan dari dokter, pasien disarankan melakukan beberapa hal berikut untuk mengurangi gatal yang muncul akibat lichen planus di kulit, yaitu :\n- Jangan menggaruk ruam.\n- Rendam ruam ke dalam bak mandi oatmeal.\n- Gunakan produk sabun dan sampo yang berbahan kimia ringan guna mencegah iritasi kulit.\n- Berikan kompres dingin di kulit yang gatal dan kemerahan.\n- Oleskan krim pelembab untuk mencegah kulit kering.'
]

info_penyakit_lichen_planus = [
    '   Lichen planus adalah peradangan di kulit, kuku, atau selaput lendir (mukosa) akibat adanya kelainan pada sistem kekebalan tubuh. Lichen planus tidak menular layaknya infeksi, tetapi bisa dialami oleh semua orang dari segala golongan usia.Lichen planus yang muncul di kulit ditandai dengan kulit yang bersisik dan ruam atau bercak berwarna merah keunguan yang umumnya terasa gatal. Sementara itu, di daerah mukosa, seperti mulut atau vagina, lichen planus ditandai dengan munculnya bercak putih yang kadang terasa nyeri.Seperti yang sudah disebutkan, lichen planus bukanlah penyakit menular. Namun, penyakit ini bisa berkembang menjadi penyakit kronis di kulit dan menyebar hingga ke area lain. Lichen planus paling sering terjadi pada orang berusia 30–60 tahun.\n\nPenyebab Lichen Planus :\nHingga saat ini, penyebab terjadinya lichen planus masih belum diketahui dengan jelas. Namun, kondisi ini diduga terjadi saat seseorang terkena gangguan autoimun, yaitu kondisi ketika sistem kekebalan tubuh secara keliru menyerang sel-sel kulit atau selaput lendir yang sehat.Selain itu, ada beberapa faktor yang diketahui dapat meningkatkan risiko seseorang untuk mengalami lichen planus, yaitu:\n- Memiliki riwayat keluarga dengan lichen planus.\n- Menderita dermatitis kontak alergi\n- Menderita penyakit infeksi, misalnya hepatitis C.\n- Mengalami efek samping obat-obatan tertentu, misalnya obat antiinflamasi nonsteroid, antimalaria, obat penurun tekanan darah, diuretik, atau obat untuk penyakit diabetes.\n- Pernah menjalani operasi transplantasi organ.\n- Terpapar logam merkuri dan emas, misalnya dari bahan tambalan gigi, perhiasan, atau cairan kimia yang digunakan dalam proses cetak foto.\n\nGejala Lichen Planus :\nGejala lichen planus bisa beragam, tergantung pada bagian tubuh mana yang mengalami kondisi ini. Berikut ini adalah beberapa gejala lichen planus yang dapat muncul, yaitu:\n  - Ruam kulit berwarna merah keunguan dan menonjol di kulit.\n  - Kulit terasa gatal dan bersisik.\n  - Mulut kering dan terasa pahit.\n  - Kuku rusak, rapuh, dan bisa lepas.\n  - Rambut rontok.\n  - Bercak putih di vagina yang disertai nyeri dan sensasi terbakar.\n  - Bercak keunguan berbentuk cincin di ujung penis yang tidak terasa nyeri.\n  - Bercak putih berbentuk seperti garis di dalam mulut (Wickham striae).\n\nKapan harus ke dokter :\nLakukan pemeriksaan diri ke dokter apabila Anda mengalami berbagai gejala lichen planus, terutama jika:\n  - Gejala muncul tanpa sebab yang jelas.\n  - Gejala berlangsung lebih lama dari yang diperkirakan.\n  - Gejala memburuk hingga menimbulkan tanda-tanda infeksi.\n  - Gejala tidak kunjung membaik setelah menjalani penanganan mandiri.\nAnda juga disarankan untuk memeriksakan diri ke dokter apabila mengalami gejala lichen planus di mulut atau vagina. Pemeriksaan dini akan membantu dokter dalam memberikan pengobatan. Dengan begitu, komplikasi dapat dicegah.'
]

solusi_penyakit_hives = [
    'Pengobatan dan Pencegahan Biduran/Hives\n\nBiduran ringan biasanya akan sembuh tanpa pengobatan. Namun, biduran yang terjadi berulang perlu ditangani dengan obat-obatan sesuai resep dokter, seperti obat antihistamin atau kortikosteroid.Menghindari suhu panas, stres, obat-obatan, atau makanan, merupakan cara efektif untuk mencegah biduran. Makanan atau obat-obatan tersebut bisa dihindari setelah dipastikan oleh dokter sebagai penyebab biduran pada pasien.'
]

info_penyakit_hives = [
    '   Biduran adalah reaksi di kulit yang ditandai dengan munculnya bentol berwarna kemerahan dan disertai rasa gatal. Biduran bisa muncul di area kulit mana saja, termasuk wajah, leher, telinga, hingga seluruh tubuh.Pada umumnya, biduran tergolong ringan dan sembuh dengan sendirinya setelah beberapa jam atau setelah mengonsumsi obat-obatan. Namun, pada beberapa kasus, biduran dapat berlangsung selama beberapa minggu dan terjadi berulang. Kondisi ini dapat disebut sebagai biduran kronis.\n\nGejala dan Penyebab Biduran :\nBiduran atau urtikaria ditandai dengan kemunculan bentol atau ruam kemerahan yang disertai rasa gatal. Berdasarkan jenisnya, biduran dapat dibagi menjadi biduran akut dan biduran kronis. Biduran akut berlangsung kurang dari 6 minggu, sedangkan biduran kronis bertahan selama lebih dari 6 minggu.Biduran merupakan reaksi alergi terhadap benda atau zat asing, yang menyebabkan sistem kekebalan tubuh mengeluarkan histamin. Histamin inilah yang menyebabkan munculnya tanda dan gejala biduran.Selain reaksi alergi, biduran dapat dicipu oleh beberapa faktor, seperti stres, reaksi terhadap suhu panas, atau penyakit tertentu, misalnya penyakit tiroid atau kanker.\n\nPengobatan dan Pencegahan Biduran :\nBiduran ringan biasanya akan sembuh tanpa pengobatan. Namun, biduran yang terjadi berulang perlu ditangani dengan obat-obatan sesuai resep dokter, seperti obat antihistamin atau kortikosteroid.Menghindari suhu panas, stres, obat-obatan, atau makanan, merupakan cara efektif untuk mencegah biduran. Makanan atau obat-obatan tersebut bisa dihindari setelah dipastikan oleh dokter sebagai penyebab biduran pada pasien.'
]

diagnosa_layout = [
    [sg.Text('PILIH GEJALA', background_color = 'Grey', text_color = 'White', border_width = 5) ],
    [sg.Listbox([
        
        '1.Rasa Panas dan dingin yang berlebihan pada bagian kulit yang terkena eksim.',
        '2.Rasa gatal terutama terasa pada malam hari.',
        '3.Tampak lepuhan-lepuhan kecil dan kulit bersisik yang keras pada permukaan kulit yang akan disertai dengan pembengkakan.',
        '4.Kulit kering, bersisik, kemerah-merahan.',
        '5.Timbul bintil-bintil yang mengandung air atau nanah.',
        '6.Ruam kemerahan.',
        '7.Peradangan.',
        '8.Gatal yang kadang-kadang terasa parah.',
        '9.Kering.',
        '10.Pembengkakan.',
        '11.Kulit kering.',
        '12.Bersisik.',
        '13.Lecet melepuh.',
        '14.Menebal.',
        '15.Pecah-pecah.',
        '16.Kulit melepuh dan berisi cairan.',
        '17.Pecahan kulit yang melepuh dan berwarna kuning.',
        '18.Munculnya bercak merah menyerupai luka yang tidak terasa sakit, namun gatal.',
        '19.Bercak bisa menyebar dalam waktu singkat ketika disentuh atau digaruk, kemudian berganti menjadi kerak berwarna kecokelatan.',
        '20.Munculnya bintik-bintik.',
        '21.Kulit berminyak.',
        '22.Sakit atau panas apabila disentuh.',
        '23.Gatal yang sangat terasa pada permukaan kulit.',
        '24.Berwarna kemerahan dan biasanya disertai infeksi lanjutan seperti yang diakibatkan oleh bakteri maupun jamur.',
        '25.Bisul pada telapak tangan atau kaki.',
        '26.Ruam kemerahan yang berbentuk cincin dengan garis luar yang tidak beraturan.',
        '27.Ruam terasa bersisik dan gatal.',
        '28.Lingkaran ruam kurap juga dapat melebar dan muncul di bagian tubuh mana saja.',
        '29.Ruam membentuk benjolan dan melepuh.',
        '30.Kulit pecah-pecah di bagian yang terinfeksi serta kulit bersisik.',
        '31.Ruam yang gatal, kering, dan terkelupas di antara jari kaki.',
        '32.Rasa gatal ketika berkeringat dan warna sebagian kulit berubah menjadi putih.',
        '33.Terdapat sisik halus yang menutupinya.',
        '34.Benjolan berwarna ungu kemerahan dengan bagian atas yang rata dan mengkilat.',
        '35.Terbentuknya sebagian kulit yang menebal dan bersisik, biasanya di sekitar pergelangan kaki.',
        '36.Terasa gatal.',
        '37.Perubahan warna kulit menjadi gelap setelah benjolan-benjolan mereda.',
        '38.Adanya warna merah pada kulit serta ruam gatal.',
        '39.Gatal-gatal disertai kemerahan pada kulit.',
        '40.Busung.',
        '41.Kulit terasa panas.',
        '42.Pembengkakan yang berlebihan dari kelopak mata.',
        '43.Kesulitan bernafas atau menelan.',
    ]
        , size=(70,8), select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, expand_x =True)
    ],

    [sg.Button('Tambahkan', expand_x =True), sg.Button('Reset', expand_x =True)],
    [sg.Text('Gejala yang anda Pilih', background_color = 'Grey', text_color = 'White', border_width = 5)],
    [sg.Multiline('', key='-TEXTADD-', no_scrollbar=True, size = (800, 10), disabled = True)],
    [sg.Button('Diagnosa', expand_x =True)],
    [sg.Text('Hasil Diagnosa', background_color = 'Grey', text_color = 'White', border_width = 5)],
    [sg.Multiline('', key='-OUTPUT-', no_scrollbar=True, size = (800, 0), disabled = True)],
    [sg.Text('Solusi', background_color = 'Grey', text_color = 'White', border_width = 5)],
    [sg.Multiline('', key='-SOLUSI-', size = (800, 20), disabled = True)]
]


form_layout = [
    [sg.Text('Formulir Pengisian Identitas Pasien', background_color = 'Grey', text_color = 'White', border_width = 5)],
    [sg.Text('Nama Pasien: ', size = (20,1)), sg.Input(key='-NAMA-', do_not_clear=True, size=(20, 1), expand_x =True,)],
    [sg.Text('Tanggal Lahir: ', size = (20,1)), sg.Input(key='-TGL-', do_not_clear=True, size=(20, 1), expand_x =True,)],
    [sg.Text('Alamat Rumah: ', size = (20,1)), sg.Input(key='-ALAMAT-', do_not_clear=True, size=(20, 1), expand_x =True,)],
    [sg.Text('Nomor Telepon: ', size = (20,1)), sg.Input(key='-NOMOR_TELEPON-', do_not_clear=True, size=(20, 1), expand_x =True,)],
    [sg.Text('Hasil Diagnosa Penyakit: ', size = (20,1)), sg.Input(key='-DIAGNOSA_PENYAKIT-', do_not_clear=True, size=(20, 1), expand_x =True,)],
    [sg.Button('Submit'), sg.Button('Clear', key='-RESET_DATA_PASIEN-')],
    [sg.Text('')],
    [sg.Text('Data Pasien', background_color = 'Grey', text_color = 'White', border_width = 5)],
    [sg.Table(
        values=data_pasien, 
        headings=title_table_pasien,
        auto_size_columns = True,
        display_row_numbers= True,
        justification = 'left',
        key = '-TABLE_PASIEN-',
        max_col_width=0,
        row_height = 40,
        expand_x =True,   
    )]

]


artikel_layout = [
    [sg.Text('Table Penyakit Kulit', background_color = 'Grey', text_color = 'White', border_width = 5)],
    [sg.Table(
        values=data_penyakit_kulit, 
        headings=title_penyakit_kulit,
        auto_size_columns = True,
        justification = 'left',
        num_rows = 5,
        max_col_width=50,
        expand_x =True,
    )],
    [sg.Text('Table Gejala', background_color = 'Grey', text_color = 'White', border_width = 5)],
    [sg.Table(
        values=data_gejala, 
        headings=title_gejala,
        auto_size_columns = True,
        justification = 'left',
        max_col_width=50,
        row_height = 35,
        expand_x =True,
        vertical_scroll_only = True,
    )],
    [sg.Text('Table Aturan', background_color = 'Grey', text_color = 'White', border_width = 5)],
    [sg.Table(
        values=data_aturan, 
        headings=title_aturan,
        auto_size_columns = True,
        justification = 'left',
        key = '-TABLE-',
        max_col_width=50,
        expand_x =True,
    )],

]

layout_p1 = [
    [sg.Multiline(
        '\n'.join(info_penyakit_eksim), 
        size = (800, 50),
        disabled = True,
    )]
    
]

layout_p2 = [
    [sg.Multiline(
        '\n'.join(info_penyakit_dermatitis), 
        size = (800, 50),
        disabled = True,
    )]
    
]

layout_p3 = [
    [sg.Multiline(
        '\n'.join(info_penyakit_impetigo), 
        size = (800, 50),
        disabled = True,
    )]
]

layout_p4 = [
    [sg.Multiline(
        '\n'.join(info_penyakit_jerawat), 
        size = (800, 50),
        disabled = True,
    )]
]


layout_p5 = [
    [sg.Multiline(
        '\n'.join(info_penyakit_kudis), 
        size = (800, 50),
        disabled = True,
    )]
]

layout_p6 = [
    [sg.Multiline(
        '\n'.join(info_penyakit_kurap), 
        size = (800, 50),
        disabled = True,
    )]
]

layout_p7 = [
    [sg.Multiline(
        '\n'.join(info_penyakit_panu), 
        size = (800, 50),
        disabled = True,
    )]
]

layout_p8 = [
    [sg.Multiline(
        '\n'.join(info_penyakit_lichen_planus), 
        size = (800, 50),
        disabled = True,
    )]
]

layout_p9 = [
    [sg.Multiline(
        '\n'.join(info_penyakit_hives), 
        size = (800, 50),
        disabled = True,
    )]
]



info_penyakit = [
    [sg.Text('Info Penyakit')],
    [sg.TabGroup(
        [[
            sg.Tab('Eksim', layout_p1),
            sg.Tab('Dermatitis', layout_p2),
            sg.Tab('Impetigo', layout_p3),
            sg.Tab('Jerawat', layout_p4),
            sg.Tab('Kudis', layout_p5),
            sg.Tab('Kurap', layout_p6),
            sg.Tab('Panu', layout_p7),
            sg.Tab('Lichen Planus', layout_p8),
            sg.Tab('Hives', layout_p9)
        ]],
        tab_location = 'topleft',
        title_color = 'White', 
        tab_background_color = 'Grey', 
        selected_title_color = 'White',
        selected_background_color = 'Black',
        expand_x='True',
        size = (50, 0)
    )]
]

about_layout = [
    [sg.Text('About Aplikasi Sistem Pakar Diagnosa Penyakit Kulit',font = 'Franklin 15')],
    [sg.Text('PERINGATAN :',font = 'Franklin 10',  text_color = 'White', background_color = 'Red', border_width = 5)],
    [sg.Text('Jangan mempercayai seratus persen dari hasil diagnosa yang ada di aplikasi sitem pakar ini, aplikasi sistem pakar diagnosa penyakit kulit bertujuan untuk memberitahu kepada masyarakat indonesia untuk lebih memperdulikan dan Mengkhawatirkan tentang penyakit kulit dan memberitahukan informasi-informasi seputar penyakit kulit.\nSesudah anda melakukan diagnosa menggunakan aplikasi diagnosa ini dan mendapatkan hasil, Sebaiknya anda mencari tahu lebih lanjut atau berkonsultasi dan melakukan pemeriksaan ke dokter spesialis kulit yang ahli, yang ada di rumah sakit disekitar tempat tinggal anda.',font = 'Franklin 10', size = (98, 0))],
    [sg.Text('')],
    [sg.Text('Informasi terkait Aplikasi Sistem Pakar Diagnosa Penyakit Kulit :',font = 'Franklin 10', text_color = 'White', background_color = 'Green', border_width = 5)],
    [sg.Text('Data penyakit,gejala dan aturan yang ada di aplikasi sistem pakar ini tidak didapatkan atau tidak melakukan penelitian melainkan menggunakan data dari jurnal yang sudah melakukan penelitian sebelumnya. Source Jurnal yang digunakan : https://jurnal.stmik-dci.ac.id/index.php/jumantaka/article/view/300',font = 'Franklin 10', size = (98, 0))],
    [sg.Text('')],
    [sg.Text('Fitur :',text_color = 'White', background_color = 'Purple', border_width = 5)],
    [sg.Text('- Diagnosa\n- Artikel\n- Info Penyakit\n- About')],
    [sg.Text('')],
    [sg.Text('')],
    [sg.Text('')],
    [sg.Text('')],
    [sg.Text('')],
    [sg.Text('')],
    [sg.Text('')],
    [sg.Text('Python Apps\nLib.PySimpleGui\nCreated bye 1Sh\nVersion : 0.1', font = 'Courier 10')],
    
]



layout = [
    [sg.Text('Aplikasi Diagnosa Penyakit kulit', 
        font = 'Franklin 20', 
        justification= 'left', 
        expand_x='True',
        )
    ],
    
    [sg.TabGroup(
        [[
            sg.Tab('Diagnosa', diagnosa_layout),
            sg.Tab('Formulir Pasien', form_layout),
            sg.Tab('Artikel', artikel_layout),
            sg.Tab('Info Penyakit', info_penyakit),
            sg.Tab('About', about_layout),
        ]],
        tab_location = 'centertop',
        title_color = 'White', 
        tab_background_color = 'Green', 
        selected_title_color = 'White',
        selected_background_color = 'Gray',
        size=(800, 0)
        
    ), 
    sg.Multiline('Logging Output : ', 
        key='-TERMINAL-', 
        font='Courier 8',
        no_scrollbar=True, 
        size = (80, 50), 
        disabled = True, 
        expand_x=True, 
        expand_y=True, 
        write_only=True,
        reroute_stdout=True, 
        reroute_stderr=True, 
        echo_stdout_stderr=True, 
        autoscroll=True, 
        auto_refresh=True)
    ],

]


window = sg.Window('Sistem Pakar Diagnosa Penyakit Kulit', layout, icon=r'C:\Users\Ace\Desktop\aplikasi-sistem-pakar-main\icon.ico', size=(1024,768))

add_gejala = []
diagnosa = []

while True:
    event, values = window.read()
    # print('Output Terminal :')
    # print('Event:',event)
    # print('-- Values Output --')
    if event == sg.WIN_CLOSED:
        break


    if event == 'Tambahkan':
        add_gejala = values[0]
        window['-TEXTADD-'].update('\n'.join(add_gejala))
        print("[LOG] Clicked Tambahkan!")

    if event == 'Submit':
        data_pasien.append([values['-NAMA-'], values['-TGL-'], values['-ALAMAT-'], values['-NOMOR_TELEPON-'], values['-DIAGNOSA_PENYAKIT-']])
        window['-TABLE_PASIEN-'].update(values=data_pasien)
        
    if event == '-RESET_DATA_PASIEN-':
        window['-NAMA-'].update('')
        window['-TGL-'].update('')
        window['-ALAMAT-'].update('')
        window['-NOMOR_TELEPON-'].update('')
        window['-DIAGNOSA_PENYAKIT-'].update('')


    if event == 'Reset':
        window['-TEXTADD-'].update('')
        window['-SOLUSI-'].update('')
        window['-OUTPUT-'].update('')
        print("[LOG] Clicked Reset!")
    

    if event == 'Diagnosa':
        print("[LOG] Clicked Diagnosa!")
        diagnosa = add_gejala
        if diagnosa == ['1.Rasa Panas dan dingin yang berlebihan pada bagian kulit yang terkena eksim.','2.Rasa gatal terutama terasa pada malam hari.','3.Tampak lepuhan-lepuhan kecil dan kulit bersisik yang keras pada permukaan kulit yang akan disertai dengan pembengkakan.','4.Kulit kering, bersisik, kemerah-merahan.','5.Timbul bintil-bintil yang mengandung air atau nanah.',]:
            window['-OUTPUT-'].update('Penyakit Eksim')
            window['-SOLUSI-'].update('\n'.join(solusi_penyakit_eksim))

        elif diagnosa == ['6.Ruam kemerahan.','7.Peradangan.','8.Gatal yang kadang-kadang terasa parah.','9.Kering.','10.Pembengkakan.','11.Kulit kering.','12.Bersisik.','13.Lecet melepuh.','14.Menebal.','15.Pecah-pecah.',]:
            window['-OUTPUT-'].update('Penyakit Dermatitis')
            window['-SOLUSI-'].update('\n'.join(solusi_penyakit_dermatitis))

        elif diagnosa == ['16.Kulit melepuh dan berisi cairan.','17.Pecahan kulit yang melepuh dan berwarna kuning.','18.Munculnya bercak merah menyerupai luka yang tidak terasa sakit, namun gatal.','19.Bercak bisa menyebar dalam waktu singkat ketika disentuh atau digaruk, kemudian berganti menjadi kerak berwarna kecokelatan.',]:
            window['-OUTPUT-'].update('Penyakit Impetigo')
            window['-SOLUSI-'].update('\n'.join(solusi_penyakit_impetigo))

        elif diagnosa == ['20.Munculnya bintik-bintik.','21.Kulit berminyak.','22.Sakit atau panas apabila disentuh.',]:
            window['-OUTPUT-'].update('Penyakit Jerawat')
            window['-SOLUSI-'].update('\n'.join(solusi_penyakit_jerawat))


        elif diagnosa == ['23.Gatal yang sangat terasa pada permukaan kulit.','24.Berwarna kemerahan dan biasanya disertai infeksi lanjutan seperti yang diakibatkan oleh bakteri maupun jamur.','25.Bisul pada telapak tangan atau kaki.']:
            window['-OUTPUT-'].update('Penyakit Kudis')
            window['-SOLUSI-'].update('\n'.join(solusi_penyakit_kudis))

        elif diagnosa == ['26.Ruam kemerahan yang berbentuk cincin dengan garis luar yang tidak beraturan.','27.Ruam terasa bersisik dan gatal.','28.Lingkaran ruam kurap juga dapat melebar dan muncul di bagian tubuh mana saja.','29.Ruam membentuk benjolan dan melepuh.','30.Kulit pecah-pecah di bagian yang terinfeksi serta kulit bersisik.','31.Ruam yang gatal, kering, dan terkelupas di antara jari kaki.']:
            window['-OUTPUT-'].update('Penyakit Kurap')
            window['-SOLUSI-'].update('\n'.join(solusi_penyakit_kurap))

        elif diagnosa == ['32.Rasa gatal ketika berkeringat dan warna sebagian kulit berubah menjadi putih.',
        '33.Terdapat sisik halus yang menutupinya.']:
            window['-OUTPUT-'].update('Penyakit Panu')
            window['-SOLUSI-'].update('\n'.join(solusi_penyakit_panu))

        elif diagnosa == ['34.Benjolan berwarna ungu kemerahan dengan bagian atas yang rata dan mengkilat.','35.Terbentuknya sebagian kulit yang menebal dan bersisik, biasanya di sekitar pergelangan kaki.','36.Terasa gatal.','37.Perubahan warna kulit menjadi gelap setelah benjolan-benjolan mereda.']:
            window['-OUTPUT-'].update('Penyakit Lichen Planus')
            window['-SOLUSI-'].update('\n'.join(solusi_penyakit_lichen_planus))

        elif diagnosa == ['38.Adanya warna merah pada kulit serta ruam gatal.','39.Gatal-gatal disertai kemerahan pada kulit.','40.Busung.','41.Kulit terasa panas.','42.Pembengkakan yang berlebihan dari kelopak mata.','43.Kesulitan bernafas atau menelan.']:
            window['-OUTPUT-'].update('Penyakit Hives')
            window['-SOLUSI-'].update('\n'.join(solusi_penyakit_hives))

        else:
            window['-OUTPUT-'].update('Tidak Ada penyakit yang sesuai dengan gejala yang anda pilih')
       

window.close()
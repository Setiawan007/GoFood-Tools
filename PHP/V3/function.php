<? php

permintaan fungsi ($ url, $ token = null, $ data = null, $ pin = null, $ otpsetpin = null, $ uuid = null) {

$ header [] = "Host: api.gojekapi.com";
$ header [] = "User-Agent: okhttp / 3.10.0";
$ header [] = "Terima: application / json";
$ header [] = "Bahasa Terima: id-ID";
$ header [] = "Tipe-Konten: application / json; charset = UTF-8";
$ header [] = "X-AppVersion: 3.56.2";
$ header [] = "X-UniqueId:" .time (). "57" .mt_rand (1000.9999);
$ header [] = "Koneksi: tetap-hidup";
$ header [] = "X-User-Lokal: id_ID";
$ header [] = "X-Location: -8.424012,115.194628";
$ header [] = "X-Location-Accuracy: 3.0";
if ($ pin):
$ header [] = "pin: $ pin";
    berakhir jika;
if ($ token):
$ header [] = "Otorisasi: Bearer $ token";
berakhir jika;
if ($ otpsetpin):
$ header [] = "otp: $ otpsetpin";
berakhir jika;
if ($ uuid):
$ header [] = "User-uuid: $ uuid";
berakhir jika;
$ c = curl_init ("https://api.gojekapi.com". $ url);
    curl_setopt ($ c, CURLOPT_FOLLOWLOCATION, true);
    curl_setopt ($ c, CURLOPT_SSL_VERIFYPEER, false);
    if ($ data):
    curl_setopt ($ c, CURLOPT_POSTFIELDS, $ data);
    curl_setopt ($ c, CURLOPT_POST, true);
    berakhir jika;
    curl_setopt ($ c, CURLOPT_SSL_VERIFYHOST, 0);
    curl_setopt ($ c, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt ($ c, CURLOPT_HEADER, true);
    curl_setopt ($ c, CURLOPT_HTTPHEADER, $ header);
    $ response = curl_exec ($ c);
    $ httpcode = curl_getinfo ($ c);
    if (! $ httpcode)
        return false;
    lain {
        $ header = substr ($ response, 0, curl_getinfo ($ c, CURLINFO_HEADER_SIZE));
        $ body = substr ($ response, curl_getinfo ($ c, CURLINFO_HEADER_SIZE));
    }
    $ json = json_decode ($ body, true);
    mengembalikan $ body;
}
menyimpan fungsi ($ nama file, $ konten)
{
    $ save = fopen ($ filename, "a");
    fputs ($ save, "$ content \ r \ n");
    fclose ($ save);
}
fungsi nama ()
    {
    $ ch = curl_init ();
    curl_setopt ($ ch, CURLOPT_URL, "http://ninjaname.horseridersupply.com/indonesian_name.php");
    curl_setopt ($ ch, CURLOPT_SSL_VERIFYPEER, 0);
    curl_setopt ($ ch, CURLOPT_SSL_VERIFYHOST, 0);
    curl_setopt ($ ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt ($ ch, CURLOPT_FOLLOWLOCATION, 1);
    $ ex = curl_exec ($ ch);
    // $ rand = json_decode ($ rnd_get, true);
    preg_match_all ('~ (& bull; (. *?) <br/> & bull;) ~', $ ex, $ name);
    return $ name [2] [mt_rand (0, 14)];
    }
function getStr ($ a, $ b, $ c) {
	$ a = @explode ($ a, $ c) [1];
	return @explode ($ b, $ a) [0];
}
function getStr1 ($ a, $ b, $ c, $ d) {
        $ a = @explode ($ a, $ c) [$ d];
        return @explode ($ b, $ a) [0];
}
warna fungsi ($ color = "default", $ text)
    {
        $ arrayColor = array (
            'grey' => '1; 30',
            'red' => '1; 31',
            'green' => '1; 32',
            'kuning' => '1; 33',
            'blue' => '1; 34',
            'ungu' => '1; 35',
            'nevy' => '1; 36',
            'white' => '1; 0',
        );  
        return "\ 033 [". $ arrayColor [$ color]. "m". $ text. "\ 033 [0m";
    }
function fetch_value ($ str, $ find_start, $ find_end) {
	$ start = @strpos ($ str, $ find_start);
	if ($ start === false) {
		kembali "";
	}
	$ length = strlen ($ find_start);
	$ end = strpos (substr ($ str, $ start + $ length), $ find_end);
	trim kembali (substr ($ str, $ start + $ length, $ end));
}
?>

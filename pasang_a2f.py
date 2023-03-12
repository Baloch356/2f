

import requests as req, re
from bs4 import BeautifulSoup as par
import spam as sp

__import__('os').system('git pull')

headers = {
	"Host":"mbasic.facebook.com",
	"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
	"origin":"https://www.facebook.com",
	"referer":"https://www.facebook.com",
	"sec-ch-ua":'";Not A Brand";v="99", "Chromium";v="94"',
	"upgrade-insecure-requests":"1",
	"user-agent":"Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5"
}

ses = req.Session()
ses.headers.update(headers)

class Main(object):
	
	def __init__(self,coki):
		self.coki = {"cookie":coki}
	def logo(self):
		logo = """
	░█████╗░██████╗░███████╗
	██╔══██╗╚════██╗██╔════╝
	███████║░░███╔═╝█████╗░░
	██╔══██║██╔══╝░░██╔══╝░░
	██║░░██║███████╗██║░░░░░
	╚═╝░░╚═╝╚══════╝╚═╝░░░░░
    Tools enable a2f Facebook, \x1b[0;92mv1.0.0\x1b[0;97m
	Developer: Latip176, Team: Marga-176
		"""
		return logo
	def cek(self):
		try:
			r = par(
				ses.get(
					"https://mbasic.facebook.com/security/2fac/setup/intro/metadata/?source=1",cookies=self.coki
				).text, 'html.parser'
			)
		except req.exceptions.TooManyRedirects:
			r = par(
				req.get(
					"https://mbasic.facebook.com/security/2fac/setup/intro/metadata/?source=1",cookies=self.coki
				).text, 'html.parser'
			)
		try:
			lanjut = r.find(
				"a",string="Use Authentication Application"
			).get(
				"href"
			)
		except:
			exit(" ! Your account has been linked with a2f ")
		try:
			__r = ses.get(lanjut,cookies=self.coki).text
		except req.exceptions.TooManyRedirects:
			__r = req.get(lanjut,cookies=self.coki).text
		co = par(__r, 'html.parser')
		try:
			kode = self.get_kode(co)
			print("\n * authentication key:",kode,"\n * Enter the authentication key in the two-factor authentication app!\n")
		except:
			if "For security purposes, please re-enter your password to continue." in __r:
				print(" * For security reasons, please enter your Facebook password to continue.")
				sandi = input(" + Password facebook: ")
				lanjut = co.find(
					'form',{
						'method':'post'
					}
				)
				memek = {}
				lst = ["fb_dtsg","jazoest","save"]
				for x in lanjut:
					if x.get("name") in lst:
						memek.update(
							{
								x.get(
									"name"
								):x.get(
									"value"
								)
							}
						)
				memek.update(
					{
						"pass":sandi
					}
				)
				response = ses.post(
					lanjut.get(
						"action"
					),cookies=self.coki,data=memek
				).text
				if "The password you entered is incorrect." in response:
					exit(" ! The password you entered is incorrect.")
				else:
					try:
						kode = self.get_kode(response)
					except IndexError:
						exit(" × Facebook affected checkpoint")
				print("\n * authentication key:",kode,"\n * Please enter the authentication key into the two-factor authentication application!\n")
			else:
				exit(" × Facebook affected checkpoint")
		self.masuk(co)
	
	def spam(self,cokii):
		print(" ! To avoid the checkpoint tools from spamming 14 comments on the author's post.\n * The process is ongoing, please wait...\n")
		sp.Main(
			cokii
		).gasken(
			14,"Latif Ganteng:v"
		)

class Pasang(Main):
	
	def pasang(self,link,data_code):
		return ses.post(
			"https://mbasic.facebook.com"+str(
				link
			),data=data_code,cookies=self.coki
		).text
	def get_kode(self,res):
		kode = re.findall(
			'\<div\ class\=\".*?\"\>Atau masukkan kode ini ke aplikasi autentikasi Anda<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>\<\/div\>',str(
				res
			)
		)[0]
		return kode
	def kode_pemulihan(self,kontol):
		num = 0
		for x in kontol.find_all('span'):
			if(
				re.findall(
					'\d+\s\d+',str(
						x
					)
				)
			):
				num+=1
				if(num==1):
					print(f" \_> {x.text}")
				else:
					print(f" |_> {x.text}")
	def get_kode_pemulihan(self):
		waifu_wangy = {
			"Host":"mbasic.facebook.com",
			"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			"content-type":"application/x-www-form-urlencoded",
			"origin":"https://www.facebook.com",
			"referer":"https://www.facebook.com",
			"upgrade-insecure-requests":"2",
			"user-agent":"Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5"
		}
		ses.headers.update(waifu_wangy)
		__res = ses.get("https://mbasic.facebook.com/security/2fac/factors/recovery-code/",cookies=self.coki).text
		kontol = par(__res, 'html.parser')
		if "Gunakan kode pemulihan untuk login jika Anda kehilangan ponsel atau tidak dapat menerima kode verifikasi melalui pesan teks atau aplikasi autentikasi." in __res:
			data = {}
			lst = ["fb_dtsg","jazoest","reset"]
			for x in kontol.find(
				'form',{
					'method':'post'
				}
			):
				if x.get('name') in lst:
					data.update(
						{x.get(
							'name'
						):x.get(
							'value'
						)
					}
				)
			data.update(
				{
					"":"Dapatkan Kode"
				}
			)
			kontol = par(
				ses.post(
					"https://mbasic.facebook.com/security/2fac/factors/recovery-code/",cookies=self.coki,data=data
				).text, 'html.parser'
			)
			self.kode_pemulihan(kontol)
		else:
			self.kode_pemulihan(kontol)
	def masuk(self,co):
		data = {}
		masuk = input(" + Masukan kode authen: ")
		lst = ["fb_dtsg","jazoest","code_handler_type","confirmButton"]
		lanjut = co.find(
			'form',{
				'method':'post'
			}
		)
		for x in lanjut:
			if x.get('name') in lst:
				data.update(
					{x.get(
						'name'
					):x.get(
						'value'
					)
				}
			)	
		data.update(
			{
				'confirmButton':'Lanjutkan'
			}
		)
		res = par(
			ses.post(
				'https://mbasic.facebook.com'+str(
					lanjut.get(
						"action"
					)
				),cookies=self.coki,data=data
			).text, 'html.parser'
		)
		data.clear()
		lanjut = res.find(
			"form",{
				"id":"input_form"
			}
		)
		lst = ["fb_dtsg","jazoest"]
		for x in lanjut:
			if x.get("name") in lst:
				data.update(
					{x.get(
						"name"
					):x.get(
						"value"
					)
				}
			)
		data.update({
			"code":masuk,
			"submit_code_button":"Lanjutkan"
		})
		response = self.pasang(
			lanjut.get(
				"action"
			),data
		)
		if "checkpoint" in response:
			exit(" × Ops akun terkena checkpoint")
		elif "Autentikasi Dua Faktor Aktif" in response:
			print(" √ a2f Berhasil di pasang ^^")
			print(" * Kode pemulihan: ")
			self.get_kode_pemulihan()
		else:
			print(" ! Text:",response)
			exit(" × Ada yang salah di script, coba laporkan ke Developer. Copy text di atas! Kirim ke wa 083172566909. ")

__import__('os').system('clear')

if __name__=="__main__":
	print(
		Pasang(
			""
		).logo(
		)
	)
	cokii = input(" + Masukan cookie: ")
	resss = req.get(
		"https://mbasic.facebook.com/profile.php",cookies={
			"cookie":cokii
		}
	).text
	if "mbasic_logout_button" in resss:
		nama = re.findall(
			'\<title\>(.*?)<\/title\>',str(
				resss
			)
		)[0]
		print(f' √ Cookies accept\n ^ Welcome {nama}\n')
		menuju = Pasang(cokii)
		menuju.spam(cokii)
		menuju.cek()
	else:
		exit(" × Cookies invalid")

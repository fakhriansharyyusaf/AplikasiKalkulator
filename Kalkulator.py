import tkinter as tk

class AplikasiKalkulator: 
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Pintar")
        self.root.geometry("350x450")
        self.root.resizable(False,False)
        
        self.string_layar = tk.StringVar()
        
        self.layar = tk.Entry(root, textvariable=self.string_layar, font=("Helvetica", 20),justify="right", bd=10)
        
        self.layar.grid(row=0, column=0, columnspan=4, ipady=15, padx=10, pady=10)
        
        self.daftar_tombol = [
            ['<=', 'AC', '%', '/'],
            ['7', '8', '9', 'x'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['+/-', '0', ',', '=']
        ]

        for i, baris in enumerate(self.daftar_tombol,start =1):
            for j, teks_tombol in enumerate(baris):
                
                warna_bg = "#e7e7e7"
                warna_fg = "black"
                if teks_tombol == '=':
                    aksi = self.hitung_hasil
                elif teks_tombol == '<=':
                    aksi = self.hapus_layar
                elif teks_tombol == 'AC': 
                    aksi = self.hapus_semua
                    warna_bg = "#f44336"
                    warna_fg =  "white"
                elif teks_tombol == '+/-':
                    aksi = self.ubah_angka
                else: 
                    aksi = lambda x=teks_tombol:self.tekan_tombol(x)
                    warna_bg = "#e7e7e7"
                    warna_fg ="black"
                    
                tombol = tk.Button(root, text=teks_tombol, font=("Helvetica", 14, "bold"), bg=warna_bg, fg=warna_fg, bd=2, width=5, height=2, command=aksi)
                
                tombol.grid(row=i, column=j, padx=5, pady=5)
    
    def tekan_tombol(self, karakter):
        teks_sekarang = self.string_layar.get()
        
        if karakter == 'x': 
            karakter == '*'
            
        elif karakter == ',':
            karakter ='.'
        
        self.string_layar.set(teks_sekarang + str(karakter))
    def hitung_hasil(self):
            try:       
                perhitungan = self.string_layar.get()
                
                perhitungan = perhitungan.replace("x", "*")
                perhitungan = perhitungan.replace(",", ".")
                if '%' in perhitungan:
                    perhitungan = perhitungan.replace('%', '/100')
                        
                hasil = eval(perhitungan)
                self.string_layar.set(hasil)
            except ZeroDivisionError:
                self.string_layer.set("Error: Div by 0")
            except Exception: 
                self.string_layer.set("Error syntax") 
        
    def hapus_layar(self):
        teks_sekarang = self.string_layar.get()
        self.string_layar.set(teks_sekarang[:-1])
        
    def hapus_semua(self):
        self.string_layar.set("")
        
    def ubah_angka(self):
        try:
            teks_sekarang = self.string_layar.get()
            if teks_sekarang: 
                if teks_sekarang.startswith('-'):
                    self.string_layar.set(teks_sekarang[1:])
                else:
                    self.string_layar.set('-' + teks_sekarang)
        except Exception: 
            pass
jendela =tk.Tk()
kalkulator = AplikasiKalkulator(jendela)
jendela.mainloop()

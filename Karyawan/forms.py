from django.forms import ModelForm

from Karyawan.models import Biodata_karyawan, Absen_karyawan, Izin_karyawan


class Karyawan_Form(ModelForm):
    class Meta:
        model = Biodata_karyawan
        fields = ['nama_karyawan', 'tanggal_lahir', 'alamat', 'telepon', 'email_karyawan', 'shift_kerja']
        labels = {

            'nama_karyawan': 'Nama Lengkap',
            'tanggal_lahir': 'Tanggal Lahir',
            'alamat': 'Alamat',
            'telepon': 'Nomer Telepon',
            'email_karyawan': 'Email',
            'shift_kerja': 'Waktu Kerja'
        }

        error_messages = {

            'nama_karyawan': {
                'required': 'Anda harus mengisi nama'
            },

            'tanggal_lahir_karyawan': {
                'required': 'Anda harus mengisi tanggal lahir'
            },

            'alamat_karyawan': {
                'required': 'Anda harus mengisi alamat'
            },
            'telepon_karyawan': {
                'required': 'Anda harus mengisi nomer telepon'
            }
        }


class Absen_karyawan_Form(ModelForm):
    class Meta:
        model = Absen_karyawan
        fields = []
        labels = {}


class Izin_karyawan_Form(ModelForm):
    class Meta:
        model = Izin_karyawan
        fields = ['jenis_kehadiran', 'waktu_berhenti', 'alasan']
        labels = {

            'jenis_kehadiran': 'Jenis Kehadiran',
            'waktu_berhenti': 'waktu_berhenti',
            'alasan': 'Alasan'

        }

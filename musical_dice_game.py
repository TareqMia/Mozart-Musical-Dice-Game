# Tareq Mia

import random
import simpleaudio as sa
import wave


mm01 = [None, None, "96", "32", "69", "40", "148", "104", "152", "119", "98", "3", "54"]
mm02 = [None, None, "22", "6", "95", "17", "74", "157", "60", "84", "142", "87", "130"]
mm03 = [None, None, "141", "128", "158", "113", "163", "27", "171", "114", "42", "165", "10"]
mm04 = [None, None, "41", "63", "13", "85", "45", "167", "53", "50", "156", "61", "103"]
mm05 = [None, None, "105", "46", "153", "161", "80", "154", "99", "140", "75", "135", "28"]
mm06 = [None, None, "122", "46", "55", "2", "97", "68", "133", "86", "129", "47", "37"]
mm07 = [None, None, "11", "134", "110", "159", "36", "118", "21", "169", "62", "147", "37"]
mm08 = [None, None, "30", "81", "24", "100", "107", "91", "127", "94", "123", "33", "5"]
mm09 = [None, None, "70", "117", "66", "90", "25", "138", "16", "120", "65", "102", "35"]
mm10 = [None, None, "121", "39", "139", "176", "143", "71", "155", "88", "77", "4", "20"]
mm11 = [None, None, "26", "126", "15", "7", "64", "150", "57", "48", "19", "31", "108"]
mm12 = [None, None, "9", "56", "132", "34", "125", "29", "175", "166", "82", "164", "92"]
mm13 = [None, None, "112", "174", "73", "67", "76", "101", "43", "51", "137", "144", "12"]
mm14 = [None, None, "49", "18", "58", "160", "136", "162", "168", "115", "38", "59", "124"]
mm15 = [None, None, "109", "116", "145", "52", "1", "23", "89", "72", "149", "173", "44"]
mm16 = [None, None, "14", "83", "79", "170", "93", "151", "172", "111", "8", "78", "131"]


minuet_table = [mm01, mm02, mm03, mm04, mm05, mm06, mm07, mm08,
            mm09, mm10, mm11, mm12, mm13, mm14, mm15, mm16]


tm01 = [None, "72", "56", "75", "40", "83", "18"]
tm02 = [None, "6", "82", "39", "73", "3", "45"]
tm03 = [None, "59", "42", "54", "16", "28", "62"]
tm04 = [None, "25", "74", "1", "68", "53", "38"]
tm05 = [None, "81", "14", "65", "29", "37", "4"]
tm06 = [None, "41", "7", "43", "55", "17", "27"]
tm07 = [None, "89", "26", "15", "2", "44", "52"]
tm08 = [None, "13", "71", "80", "61", "70", "94"]
tm09 = [None, "36", "76", "9", "22", "63", "11"]
tm10 = [None, "5", "20", "34", "67", "85", "92"]
tm11 = [None, "46", "64", "93", "49", "32", "24"]
tm12 = [None, "79", "84", "48", "77", "96", "86"]
tm13 = [None, "30", "8", "69", "57", "12", "51"]
tm14 = [None, "95", "35", "58", "87", "23", "60"]
tm15 = [None, "19", "47", "90", "33", "50", "78"]
tm16 = [None, "66", "88", "21", "10", "91", "31"]


trio_table = [tm01, tm02, tm03, tm04, tm05, tm06, tm07, tm08,
              tm09, tm10, tm11, tm12, tm13, tm14, tm15, tm16]


def minuet_filename(mmid):
    return "M" + mmid + ".wav"


def trio_filename(tmid):
      return "T" + tmid +".wav"


def roll_dice(num = 1):
    a = random.randrange(1, 7)
    b = random.randrange(2, 13)
    if num == 1:
        return a
    else:
        return b 
        

def construct_waltz():
    m_files_to_load = []
    t_files_to_load = []
    
    # sets up list of minuet files that are chosen
    for x in range(len(minuet_table)):
        m_files_to_load.append((minuet_table[x])[roll_dice(2)])
    # sets up list of trio files that are chosen
    for x in range(len(trio_table)):
        t_files_to_load.append((trio_table[x])[roll_dice(1)])
    
    # converts to proper file format
    for x in range(len(m_files_to_load)):
        m_files_to_load[x] = minuet_filename(m_files_to_load[x])
        
    for x in range(len(t_files_to_load)):
        t_files_to_load[x] = trio_filename(t_files_to_load[x])
        
    sounds = []
    for i in range(16):
        path_to_file = m_files_to_load[i]
        wave_read = wave.open(path_to_file, 'rb')
        wave_obj = sa.WaveObject.from_wave_read(wave_read)
        sounds.append(wave_obj)

    for i in range(16):
        path_to_file = t_files_to_load[i]
        wave_read = wave.open(path_to_file, 'rb')
        wave_obj = sa.WaveObject.from_wave_read(wave_read)
        sounds.append(wave_obj)

    bytes = bytearray()
    channel = 0
    bps = 0
    sr = 0


    for sound in sounds:

        bytes+= sound.audio_data
        channel = sound.num_channels
        bps = sound.bytes_per_sample
        sr = sound.sample_rate

    player = sa.play_buffer(bytes, channel, bps, sr)
    player.wait_done()
        
    return "Playing waltz"         
    
        
print(construct_waltz())

if __name__ == "__main__":
    construct_waltz()

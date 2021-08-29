import requests
import json
from matplotlib import cm

#defining variables:
debugOutput = False
on = True
bri = 255
rgb = [[]]

#defining WLED instances:
wled_instance_1 = 'http://192.168.178.190/json/state'
wled_instance_2 = 'http://192.168.178.191/json/state'
wled_instance_3 = 'http://192.168.178.192/json/state'
wled_instance_4 = 'http://192.168.178.193/json/state'
wled_instance_5 = 'http://192.168.178.194/json/state'
wled_instance_6 = 'http://192.168.178.195/json/state'
wled_controll_unit_instance = 'http://192.168.178.196/json/state'



#define the start/stop led for each segment
seg1start_wled_instance, seg1stop_wled_instance = 0, 36
seg2start_wled_instance, seg2stop_wled_instance = seg1stop_wled_instance, 76
seg3start_wled_instance, seg3stop_wled_instance = seg2stop_wled_instance, 156
seg4start_wled_instance, seg4stop_wled_instance = seg3stop_wled_instance, 232
seg5start_wled_instance, seg5stop_wled_instance = seg4stop_wled_instance, 308
seg6start_wled_instance, seg6stop_wled_instance = seg5stop_wled_instance, 384
seg7start_wled_instance, seg7stop_wled_instance = seg6stop_wled_instance, 460
seg8start_wled_instance, seg8stop_wled_instance = seg7stop_wled_instance, 536
seg9start_wled_instance, seg9stop_wled_instance = seg8stop_wled_instance, 608

#define brightness of each segment
bri_seg1_wled_instance_1 = 255
bri_seg2_wled_instance_1 = 255
bri_seg3_wled_instance_1 = 255
bri_seg4_wled_instance_1 = 255
bri_seg5_wled_instance_1 = 255
bri_seg6_wled_instance_1 = 255
bri_seg7_wled_instance_1 = 255
bri_seg8_wled_instance_1 = 255
bri_seg9_wled_instance_1 = 255

bri_seg1_wled_instance_2 = 255
bri_seg2_wled_instance_2 = 255
bri_seg3_wled_instance_2 = 255
bri_seg4_wled_instance_2 = 255
bri_seg5_wled_instance_2 = 255
bri_seg6_wled_instance_2 = 255
bri_seg7_wled_instance_2 = 255
bri_seg8_wled_instance_2 = 255
bri_seg9_wled_instance_2 = 255

bri_seg1_wled_instance_3 = 255
bri_seg2_wled_instance_3 = 255
bri_seg3_wled_instance_3 = 255
bri_seg4_wled_instance_3 = 255
bri_seg5_wled_instance_3 = 255
bri_seg6_wled_instance_3 = 255
bri_seg7_wled_instance_3 = 255
bri_seg8_wled_instance_3 = 255
bri_seg9_wled_instance_3 = 255

bri_seg1_wled_instance_4 = 255
bri_seg2_wled_instance_4 = 255
bri_seg3_wled_instance_4 = 255
bri_seg4_wled_instance_4 = 255
bri_seg5_wled_instance_4 = 255
bri_seg6_wled_instance_4 = 255
bri_seg7_wled_instance_4 = 255
bri_seg8_wled_instance_4 = 255
bri_seg9_wled_instance_4 = 255

bri_seg1_wled_instance_5 = 255
bri_seg2_wled_instance_5 = 255
bri_seg3_wled_instance_5 = 255
bri_seg4_wled_instance_5 = 255
bri_seg5_wled_instance_5 = 255
bri_seg6_wled_instance_5 = 255
bri_seg7_wled_instance_5 = 255
bri_seg8_wled_instance_5 = 255
bri_seg9_wled_instance_5 = 255

bri_seg1_wled_instance_6 = 255
bri_seg2_wled_instance_6 = 255
bri_seg3_wled_instance_6 = 255
bri_seg4_wled_instance_6 = 255
bri_seg5_wled_instance_6 = 255
bri_seg6_wled_instance_6 = 255
bri_seg7_wled_instance_6 = 255
bri_seg8_wled_instance_6 = 255
bri_seg9_wled_instance_6 = 255


#define color of each segment
rgb_seg1_wled_instance_1 = [0, 0, 0, 255]
rgb_seg2_wled_instance_1 = [0, 0, 0, 255]
rgb_seg3_wled_instance_1 = [0, 0, 0, 255]
rgb_seg4_wled_instance_1 = [0, 0, 0, 255]
rgb_seg5_wled_instance_1 = [0, 0, 0, 255]
rgb_seg6_wled_instance_1 = [0, 0, 0, 255]
rgb_seg7_wled_instance_1 = [0, 0, 0, 255]
rgb_seg8_wled_instance_1 = [0, 0, 0, 255]
rgb_seg9_wled_instance_1 = [0, 0, 0, 255]

rgb_seg1_wled_instance_2 = [0, 0, 0, 255]
rgb_seg2_wled_instance_2 = [0, 0, 0, 255]
rgb_seg3_wled_instance_2 = [0, 0, 0, 255]
rgb_seg4_wled_instance_2 = [0, 0, 0, 255]
rgb_seg5_wled_instance_2 = [0, 0, 0, 255]
rgb_seg6_wled_instance_2 = [0, 0, 0, 255]
rgb_seg7_wled_instance_2 = [0, 0, 0, 255]
rgb_seg8_wled_instance_2 = [0, 0, 0, 255]
rgb_seg9_wled_instance_2 = [0, 0, 0, 255]

rgb_seg1_wled_instance_3 = [0, 0, 0, 255]
rgb_seg2_wled_instance_3 = [0, 0, 0, 255]
rgb_seg3_wled_instance_3 = [0, 0, 0, 255]
rgb_seg4_wled_instance_3 = [0, 0, 0, 255]
rgb_seg5_wled_instance_3 = [0, 0, 0, 255]
rgb_seg6_wled_instance_3 = [0, 0, 0, 255]
rgb_seg7_wled_instance_3 = [0, 0, 0, 255]
rgb_seg8_wled_instance_3 = [0, 0, 0, 255]
rgb_seg9_wled_instance_3 = [0, 0, 0, 255]

rgb_seg1_wled_instance_4 = [0, 0, 0, 255]
rgb_seg2_wled_instance_4 = [0, 0, 0, 255]
rgb_seg3_wled_instance_4 = [0, 0, 0, 255]
rgb_seg4_wled_instance_4 = [0, 0, 0, 255]
rgb_seg5_wled_instance_4 = [0, 0, 0, 255]
rgb_seg6_wled_instance_4 = [0, 0, 0, 255]
rgb_seg7_wled_instance_4 = [0, 0, 0, 255]
rgb_seg8_wled_instance_4 = [0, 0, 0, 255]
rgb_seg9_wled_instance_4 = [0, 0, 0, 255]

rgb_seg1_wled_instance_5 = [0, 0, 0, 255]
rgb_seg2_wled_instance_5 = [0, 0, 0, 255]
rgb_seg3_wled_instance_5 = [0, 0, 0, 255]
rgb_seg4_wled_instance_5 = [0, 0, 0, 255]
rgb_seg5_wled_instance_5 = [0, 0, 0, 255]
rgb_seg6_wled_instance_5 = [0, 0, 0, 255]
rgb_seg7_wled_instance_5 = [0, 0, 0, 255]
rgb_seg8_wled_instance_5 = [0, 0, 0, 255]
rgb_seg9_wled_instance_5 = [0, 0, 0, 255]

rgb_seg1_wled_instance_6 = [0, 0, 0, 255]
rgb_seg2_wled_instance_6 = [0, 0, 0, 255]
rgb_seg3_wled_instance_6 = [0, 0, 0, 255]
rgb_seg4_wled_instance_6 = [0, 0, 0, 255]
rgb_seg5_wled_instance_6 = [0, 0, 0, 255]
rgb_seg6_wled_instance_6 = [0, 0, 0, 255]
rgb_seg7_wled_instance_6 = [0, 0, 0, 255]
rgb_seg8_wled_instance_6 = [0, 0, 0, 255]
rgb_seg9_wled_instance_6 = [0, 0, 0, 255]

#define effect of each segment
effect_seg1_wled_instance_1 = 0
effect_seg2_wled_instance_1 = 0
effect_seg3_wled_instance_1 = 0
effect_seg4_wled_instance_1 = 0
effect_seg5_wled_instance_1 = 0
effect_seg6_wled_instance_1 = 0
effect_seg7_wled_instance_1 = 0
effect_seg8_wled_instance_1 = 0
effect_seg9_wled_instance_1 = 0

effect_seg1_wled_instance_2 = 0
effect_seg2_wled_instance_2 = 0
effect_seg3_wled_instance_2 = 0
effect_seg4_wled_instance_2 = 0
effect_seg5_wled_instance_2 = 0
effect_seg6_wled_instance_2 = 0
effect_seg7_wled_instance_2 = 0
effect_seg8_wled_instance_2 = 0
effect_seg9_wled_instance_2 = 0

effect_seg1_wled_instance_3 = 0
effect_seg2_wled_instance_3 = 0
effect_seg3_wled_instance_3 = 0
effect_seg4_wled_instance_3 = 0
effect_seg5_wled_instance_3 = 0
effect_seg6_wled_instance_3 = 0
effect_seg7_wled_instance_3 = 0
effect_seg8_wled_instance_3 = 0
effect_seg9_wled_instance_3 = 0

effect_seg1_wled_instance_4 = 0
effect_seg2_wled_instance_4 = 0
effect_seg3_wled_instance_4 = 0
effect_seg4_wled_instance_4 = 0
effect_seg5_wled_instance_4 = 0
effect_seg6_wled_instance_4 = 0
effect_seg7_wled_instance_4 = 0
effect_seg8_wled_instance_4 = 0
effect_seg9_wled_instance_4 = 0

effect_seg1_wled_instance_5 = 0
effect_seg2_wled_instance_5 = 0
effect_seg3_wled_instance_5 = 0
effect_seg4_wled_instance_5 = 0
effect_seg5_wled_instance_5 = 0
effect_seg6_wled_instance_5 = 0
effect_seg7_wled_instance_5 = 0
effect_seg8_wled_instance_5 = 0
effect_seg9_wled_instance_5 = 0

effect_seg1_wled_instance_6 = 0
effect_seg2_wled_instance_6 = 0
effect_seg3_wled_instance_6 = 0
effect_seg4_wled_instance_6 = 0
effect_seg5_wled_instance_6 = 0
effect_seg6_wled_instance_6 = 0
effect_seg7_wled_instance_6 = 0
effect_seg8_wled_instance_6 = 0
effect_seg9_wled_instance_6 = 0

while True:
    try:
        open_file = open("serialread.txt", 'r')
        serial_read = open_file.readlines()

        main_serial_data = serial_read[0]
        effect_serial_data = serial_read[2]

        print(main_serial_data)
        print(effect_serial_data)


        #read potentiometer brightness value
        serialReadBrightness = main_serial_data[23:26]

        #serial communictaion error handling
        if (serialReadBrightness == ''):
            serialReadBrightness = '0'
            print("corrected PotBrightness value")

        PotBrightness = int(serialReadBrightness)


        print("PotBrightness Value: ",PotBrightness)

        # read potentiometer color W value
        serialReadColorW = main_serial_data[68:71]

        # serial communictaion error handling
        if (serialReadColorW == ''):
            serialReadColorW = '0'
            print("corrected serialReadColorW value")

        PotColorW = int(serialReadColorW)

        print("PotColorW Value: ", PotColorW)

        # read potentiometer color (RGB only) value
        serialReadColorRGB = main_serial_data[45:48]

        # serial communictaion error handling
        if (serialReadColorRGB == ''):
            serialReadColorRGB = '0'
            print("corrected serialReadColorRGB value")


        if (int(serialReadColorRGB) == 0): #handling only colorW support
            pot_rgb = [0, 0, 0, PotColorW]
        else:
            PotColorRGB = int(float(serialReadColorRGB))

            print("PotColorRGB Value: ", PotColorRGB)

            pot_values = [PotColorRGB]
            pot_rgbRAW = []
            for x in pot_values:
                val = cm.jet(float(x) / 255)[:3]  # The 4th element is gamma
                pot_rgbRAW.append([round(x * 255) for x in val])
                pot_rgbRAW2 = str(pot_rgbRAW)[2:-2] #making the list a str for adding colorW value...
                pot_rgb = [int(float(i)) for i in pot_rgbRAW2.split(',')]

                #print("calculated RGB value: ", pot_rgb) #prints out the calculated RGB values...

                #!IMPORTANT! inserting color W value to colorRGB value:
                pot_rgb.insert(3, PotColorW)
                print("calculated RGBW value: ", pot_rgb)  # prints out the calculated RGB values...

            # read rotary encoder effect value
        serialReadEffect = effect_serial_data[11:14]

        # serial communictaion error handling
        if (serialReadEffect == ''):
            serialReadEffect = '0'
            print("corrected serialReadEffect value")

        enc_effect = int(serialReadEffect)
        print("serialReadEffect Value: ", enc_effect)


        #MAIN CODE START - Checking selected buttons:

        #segment 1:
        buttonSegment1state = main_serial_data[93:93+1]

        if (buttonSegment1state == '1'):
            # set brightness of segment via potentiometer
            bri_seg1_wled_instance_1 = PotBrightness
            rgb_seg1_wled_instance_1 = pot_rgb
            effect_seg1_wled_instance_1 = enc_effect

        #segment 2:
        buttonSegment2state = main_serial_data[116:116+1]

        if (buttonSegment2state == '1'):
            # set brightness of segment via potentiometer
            bri_seg2_wled_instance_1 = PotBrightness
            rgb_seg2_wled_instance_1 = pot_rgb
            effect_seg2_wled_instance_1 = enc_effect

        #segment 3:
        buttonSegment3state = main_serial_data[139:139+1]

        if (buttonSegment3state == '1'):
            # set brightness of segment 3 via potentiometer
            bri_seg3_wled_instance_1 = PotBrightness
            rgb_seg3_wled_instance_1 = pot_rgb
            effect_seg3_wled_instance_1 = enc_effect

        #segment 4:
        buttonSegment4state = main_serial_data[162:162+1]

        if (buttonSegment4state == '1'):
            # set brightness of segment 4 via potentiometer
            bri_seg4_wled_instance_1 = PotBrightness
            rgb_seg4_wled_instance_1 = pot_rgb
            effect_seg4_wled_instance_1 = enc_effect

        #segment 5:
        buttonSegment5state = main_serial_data[185:185+1]

        if (buttonSegment5state == '1'):
            # set brightness of segment 5 via potentiometer
            bri_seg5_wled_instance_1 = PotBrightness
            rgb_seg5_wled_instance_1 = pot_rgb
            effect_seg5_wled_instance_1 = enc_effect

        #segment 6:
        buttonSegment6state = main_serial_data[208:208+1]

        if (buttonSegment6state == '1'):
            # set brightness of segment 6 via potentiometer
            bri_seg6_wled_instance_1 = PotBrightness
            rgb_seg6_wled_instance_1 = pot_rgb
            effect_seg6_wled_instance_1 = enc_effect#

        #segment 7:
        buttonSegment7state = main_serial_data[231:231+1]

        if (buttonSegment7state == '1'):
            # set brightness of segment 7 via potentiometer
            bri_seg7_wled_instance_1 = PotBrightness
            rgb_seg7_wled_instance_1 = pot_rgb
            effect_seg7_wled_instance_1 = enc_effect

        #segment 8:
        buttonSegment8state = main_serial_data[254:254+1]

        if (buttonSegment8state == '1'):
            # set brightness of segment 8 via potentiometer
            bri_seg8_wled_instance_1 = PotBrightness
            rgb_seg8_wled_instance_1 = pot_rgb
            effect_seg8_wled_instance_1 = enc_effect

        #segment 9:
        buttonSegment9state = main_serial_data[277:277+1]

        if (buttonSegment9state == '1'):
            # set brightness of segment 9 via potentiometer
            bri_seg9_wled_instance_1 = PotBrightness
            rgb_seg9_wled_instance_1 = pot_rgb
            effect_seg9_wled_instance_1 = enc_effect

        #segment 10:
        buttonSegment10state = main_serial_data[301:301+1]

        if (buttonSegment10state == '1'):
            # set brightness of segment 10 via potentiometer
            bri_seg1_wled_instance_2 = PotBrightness
            rgb_seg1_wled_instance_2 = pot_rgb
            effect_seg1_wled_instance_2 = enc_effect

        #segment 11:
        buttonSegment11state = main_serial_data[325:325+1]

        if (buttonSegment11state == '1'):
            # set brightness of segment 11 via potentiometer
            bri_seg2_wled_instance_2 = PotBrightness
            rgb_seg2_wled_instance_2 = pot_rgb
            effect_seg2_wled_instance_2 = enc_effect

        #segment 12:
        buttonSegment12state = main_serial_data[349:349+1]

        if (buttonSegment12state == '1'):
            # set brightness of segment 12 via potentiometer
            bri_seg3_wled_instance_2 = PotBrightness
            rgb_seg3_wled_instance_2 = pot_rgb
            effect_seg3_wled_instance_2 = enc_effect

        #segment 13:
        buttonSegment13state = main_serial_data[373:373+1]

        if (buttonSegment13state == '1'):
            # set brightness of segment 13 via potentiometer
            bri_seg4_wled_instance_2 = PotBrightness
            rgb_seg4_wled_instance_2 = pot_rgb
            effect_seg4_wled_instance_2 = enc_effect

        #segment 14:
        buttonSegment14state = main_serial_data[397:397+1]

        if (buttonSegment14state == '1'):
            # set brightness of segment 14 via potentiometer
            bri_seg5_wled_instance_2 = PotBrightness
            rgb_seg5_wled_instance_2 = pot_rgb
            effect_seg5_wled_instance_2 = enc_effect

        #segment 15:
        buttonSegment15state = main_serial_data[421:421+1]

        if (buttonSegment15state == '1'):
            # set brightness of segment 15 via potentiometer
            bri_seg6_wled_instance_2 = PotBrightness
            rgb_seg6_wled_instance_2 = pot_rgb
            effect_seg6_wled_instance_2 = enc_effect

        #segment 16:
        buttonSegment16state = main_serial_data[445:445+1]

        if (buttonSegment16state == '1'):
            # set brightness of segment 16 via potentiometer
            bri_seg7_wled_instance_2 = PotBrightness
            rgb_seg7_wled_instance_2 = pot_rgb
            effect_seg7_wled_instance_2 = enc_effect

        #segment 17:
        buttonSegment17state = main_serial_data[469:469+1]

        if (buttonSegment17state == '1'):
            # set brightness of segment 17 via potentiometer
            bri_seg8_wled_instance_2 = PotBrightness
            rgb_seg8_wled_instance_2 = pot_rgb
            effect_seg8_wled_instance_2 = enc_effect

        #segment 18:
        buttonSegment18state = main_serial_data[493:493+1]

        if (buttonSegment18state == '1'):
            # set brightness of segment 18 via potentiometer
            bri_seg9_wled_instance_2 = PotBrightness
            rgb_seg9_wled_instance_2 = pot_rgb
            effect_seg9_wled_instance_2 = enc_effect

        #segment 19:
        buttonSegment19state = main_serial_data[517:517+1]

        if (buttonSegment19state == '1'):
            # set brightness of segment 19 via potentiometer
            bri_seg1_wled_instance_3 = PotBrightness
            rgb_seg1_wled_instance_3 = pot_rgb
            effect_seg1_wled_instance_3 = enc_effect

        #segment 20:
        buttonSegment20state = main_serial_data[541:541+1]

        if (buttonSegment20state == '1'):
            # set brightness of segment 20 via potentiometer
            bri_seg2_wled_instance_3 = PotBrightness
            rgb_seg2_wled_instance_3 = pot_rgb
            effect_seg2_wled_instance_3 = enc_effect

        #segment 21:
        buttonSegment21state = main_serial_data[565:565+1]

        if (buttonSegment21state == '1'):
            # set brightness of segment 21 via potentiometer
            bri_seg3_wled_instance_3 = PotBrightness
            rgb_seg3_wled_instance_3 = pot_rgb
            effect_seg3_wled_instance_3 = enc_effect

        #segment 22:
        buttonSegment22state = main_serial_data[589:589+1]

        if (buttonSegment22state == '1'):
            # set brightness of segment 22 via potentiometer
            bri_seg4_wled_instance_3 = PotBrightness
            rgb_seg4_wled_instance_3 = pot_rgb
            effect_seg4_wled_instance_3 = enc_effect

        #segment 23:
        buttonSegment23state = main_serial_data[613:613+1]

        if (buttonSegment23state == '1'):
            # set brightness of segment 23 via potentiometer
            bri_seg5_wled_instance_3 = PotBrightness
            rgb_seg5_wled_instance_3 = pot_rgb
            effect_seg5_wled_instance_3 = enc_effect

        #segment 24:
        buttonSegment24state = main_serial_data[637:637+1]

        if (buttonSegment24state == '1'):
            # set brightness of segment 24 via potentiometer
            bri_seg6_wled_instance_3 = PotBrightness
            rgb_seg6_wled_instance_3 = pot_rgb
            effect_seg6_wled_instance_3 = enc_effect

        #segment 25:
        buttonSegment25state = main_serial_data[661:661+1]

        if (buttonSegment25state == '1'):
            # set brightness of segment 25 via potentiometer
            bri_seg7_wled_instance_3 = PotBrightness
            rgb_seg7_wled_instance_3 = pot_rgb
            effect_seg7_wled_instance_3 = enc_effect

        #segment 26:
        buttonSegment26state = main_serial_data[685:685+1]

        if (buttonSegment26state == '1'):
            # set brightness of segment 26 via potentiometer
            bri_seg8_wled_instance_3 = PotBrightness
            rgb_seg8_wled_instance_3 = pot_rgb
            effect_seg8_wled_instance_3 = enc_effect

        #segment 27:
        buttonSegment27state = main_serial_data[709:709+1]

        if (buttonSegment27state == '1'):
            # set brightness of segment 27 via potentiometer
            bri_seg9_wled_instance_3 = PotBrightness
            rgb_seg9_wled_instance_3 = pot_rgb
            effect_seg9_wled_instance_3 = enc_effect

        #segment 28:
        buttonSegment28state = main_serial_data[733:733+1]

        if (buttonSegment28state == '1'):
            # set brightness of segment 28 via potentiometer
            bri_seg1_wled_instance_4 = PotBrightness
            rgb_seg1_wled_instance_4 = pot_rgb
            effect_seg1_wled_instance_4 = enc_effect

        #segment 29:
        buttonSegment29state = main_serial_data[757:757+1]

        if (buttonSegment29state == '1'):
            # set brightness of segment 29 via potentiometer
            bri_seg2_wled_instance_4 = PotBrightness
            rgb_seg2_wled_instance_4 = pot_rgb
            effect_seg2_wled_instance_4 = enc_effect

        #segment 30:
        buttonSegment30state = main_serial_data[781:781+1]

        if (buttonSegment30state == '1'):
            # set brightness of segment 30 via potentiometer
            bri_seg3_wled_instance_4 = PotBrightness
            rgb_seg3_wled_instance_4 = pot_rgb
            effect_seg3_wled_instance_4 = enc_effect

        #segment 31:
        buttonSegment31state = main_serial_data[805:805+1]

        if (buttonSegment31state == '1'):
            # set brightness of segment 31 via potentiometer
            bri_seg4_wled_instance_4 = PotBrightness
            rgb_seg4_wled_instance_4 = pot_rgb
            effect_seg4_wled_instance_4 = enc_effect

        #segment 32:
        buttonSegment32state = main_serial_data[829:829+1]

        if (buttonSegment32state == '1'):
            # set brightness of segment 32 via potentiometer
            bri_seg5_wled_instance_4 = PotBrightness
            rgb_seg5_wled_instance_4 = pot_rgb
            effect_seg5_wled_instance_4 = enc_effect

        #segment 33:
        buttonSegment33state = main_serial_data[853:853+1]

        if (buttonSegment33state == '1'):
            # set brightness of segment 33 via potentiometer
            bri_seg6_wled_instance_4 = PotBrightness
            rgb_seg6_wled_instance_4 = pot_rgb
            effect_seg6_wled_instance_4 = enc_effect

        #segment 34:
        buttonSegment34state = main_serial_data[877:877+1]

        if (buttonSegment34state == '1'):
            # set brightness of segment 34 via potentiometer
            bri_seg7_wled_instance_4 = PotBrightness
            rgb_seg7_wled_instance_4 = pot_rgb
            effect_seg7_wled_instance_4 = enc_effect

        #segment 34:
        buttonSegment34state = main_serial_data[901:901+1]

        if (buttonSegment34state == '1'):
            # set brightness of segment 34 via potentiometer
            bri_seg8_wled_instance_4 = PotBrightness
            rgb_seg8_wled_instance_4 = pot_rgb
            effect_seg8_wled_instance_4 = enc_effect

        #segment 36:
        buttonSegment36state = main_serial_data[925:925+1]

        if (buttonSegment36state == '1'):
            # set brightness of segment 36 via potentiometer
            bri_seg9_wled_instance_4 = PotBrightness
            rgb_seg9_wled_instance_4 = pot_rgb
            effect_seg9_wled_instance_4 = enc_effect

        #segment 37:
        buttonSegment37state = main_serial_data[949:949+1]

        if (buttonSegment37state == '1'):
            # set brightness of segment 37 via potentiometer
            bri_seg1_wled_instance_5 = PotBrightness
            rgb_seg1_wled_instance_5 = pot_rgb
            effect_seg1_wled_instance_5 = enc_effect

        #segment 38:
        buttonSegment38state = main_serial_data[973:973+1]

        if (buttonSegment38state == '1'):
            # set brightness of segment 38 via potentiometer
            bri_seg2_wled_instance_5 = PotBrightness
            rgb_seg2_wled_instance_5 = pot_rgb
            effect_seg2_wled_instance_5 = enc_effect

        #segment 39:
        buttonSegment39state = main_serial_data[997:997+1]

        if (buttonSegment39state == '1'):
            # set brightness of segment 39 via potentiometer
            bri_seg3_wled_instance_5 = PotBrightness
            rgb_seg3_wled_instance_5 = pot_rgb
            effect_seg3_wled_instance_5 = enc_effect

        #segment 40:
        buttonSegment40state = main_serial_data[1021:1021+1]

        if (buttonSegment40state == '1'):
            # set brightness of segment 40 via potentiometer
            bri_seg4_wled_instance_5 = PotBrightness
            rgb_seg4_wled_instance_5 = pot_rgb
            effect_seg4_wled_instance_5 = enc_effect

        #segment 41:
        buttonSegment41state = main_serial_data[1045:1045+1]

        if (buttonSegment41state == '1'):
            # set brightness of segment 41 via potentiometer
            bri_seg5_wled_instance_5 = PotBrightness
            rgb_seg5_wled_instance_5 = pot_rgb
            effect_seg5_wled_instance_5 = enc_effect

        #segment 42:
        buttonSegment42state = main_serial_data[1069:1069+1]

        if (buttonSegment42state == '1'):
            # set brightness of segment 42 via potentiometer
            bri_seg6_wled_instance_5 = PotBrightness
            rgb_seg6_wled_instance_5 = pot_rgb
            effect_seg6_wled_instance_5 = enc_effect

        #segment 43:
        buttonSegment43state = main_serial_data[1093:1093+1]

        if (buttonSegment43state == '1'):
            # set brightness of segment 43 via potentiometer
            bri_seg7_wled_instance_5 = PotBrightness
            rgb_seg7_wled_instance_5 = pot_rgb
            effect_seg7_wled_instance_5 = enc_effect

        #segment 44:
        buttonSegment44state = main_serial_data[1117:1117+1]

        if (buttonSegment44state == '1'):
            # set brightness of segment 44 via potentiometer
            bri_seg8_wled_instance_5 = PotBrightness
            rgb_seg8_wled_instance_5 = pot_rgb
            effect_seg8_wled_instance_5 = enc_effect

        #segment 45:
        buttonSegment45state = main_serial_data[1141:1141+1]

        if (buttonSegment45state == '1'):
            # set brightness of segment 45 via potentiometer
            bri_seg9_wled_instance_5 = PotBrightness
            rgb_seg9_wled_instance_5 = pot_rgb
            effect_seg9_wled_instance_5 = enc_effect

        #segment 46:
        buttonSegment46state = main_serial_data[1165:1165+1]

        if (buttonSegment46state == '1'):
            # set brightness of segment 46 via potentiometer
            bri_seg1_wled_instance_6 = PotBrightness
            rgb_seg1_wled_instance_6 = pot_rgb
            effect_seg1_wled_instance_6 = enc_effect

        #segment 47:
        buttonSegment47state = main_serial_data[1189:1189+1]

        if (buttonSegment47state == '1'):
            # set brightness of segment 47 via potentiometer
            bri_seg2_wled_instance_6 = PotBrightness
            rgb_seg2_wled_instance_6 = pot_rgb
            effect_seg2_wled_instance_6 = enc_effect

        #segment 48:
        buttonSegment48state = main_serial_data[1213:1213+1]

        if (buttonSegment48state == '1'):
            # set brightness of segment 48 via potentiometer
            bri_seg3_wled_instance_6 = PotBrightness
            rgb_seg3_wled_instance_6 = pot_rgb
            effect_seg3_wled_instance_6 = enc_effect

        #segment 49:
        buttonSegment49state = main_serial_data[1237:1237+1]

        if (buttonSegment49state == '1'):
            # set brightness of segment 49 via potentiometer
            bri_seg4_wled_instance_6 = PotBrightness
            rgb_seg4_wled_instance_6 = pot_rgb
            effect_seg4_wled_instance_6 = enc_effect

        #segment 50:
        buttonSegment50state = main_serial_data[1261:1261+1]

        if (buttonSegment50state == '1'):
            # set brightness of segment 50 via potentiometer
            bri_seg5_wled_instance_6 = PotBrightness
            rgb_seg5_wled_instance_6 = pot_rgb
            effect_seg5_wled_instance_6 = enc_effect

        #segment 51:
        buttonSegment51state = main_serial_data[1285:1285+1]

        if (buttonSegment51state == '1'):
            # set brightness of segment 51 via potentiometer
            bri_seg6_wled_instance_6 = PotBrightness
            rgb_seg6_wled_instance_6 = pot_rgb
            effect_seg6_wled_instance_6 = enc_effect

        #segment 52:
        buttonSegment52state = main_serial_data[1309:1309+1]

        if (buttonSegment52state == '1'):
            # set brightness of segment 52 via potentiometer
            bri_seg7_wled_instance_6 = PotBrightness
            rgb_seg7_wled_instance_6 = pot_rgb
            effect_seg7_wled_instance_6 = enc_effect

        #segment 53:
        buttonSegment53state = main_serial_data[1333:1333+1]

        if (buttonSegment53state == '1'):
            # set brightness of segment 53 via potentiometer
            bri_seg8_wled_instance_6 = PotBrightness
            rgb_seg8_wled_instance_6 = pot_rgb
            effect_seg8_wled_instance_6 = enc_effect

        #segment 54:
        buttonSegment54state = main_serial_data[1357:1357+1]

        if (buttonSegment54state == '1'):
            # set brightness of segment 54 via potentiometer
            bri_seg9_wled_instance_6 = PotBrightness
            rgb_seg9_wled_instance_6 = pot_rgb
            effect_seg9_wled_instance_6 = enc_effect

        #mainbutton:
        mainbuttonstate = main_serial_data[1376:1376+1]
        state = False
        if (mainbuttonstate == '1'):
            # set brightness of all segments to 0
            state = True
            print(state)


        print("serial was prepared...")


        #preparing payload json post to send to wled_instance_1:
        payload_seg1_wled_instance_1 = {"start": seg1start_wled_instance, "stop": seg1stop_wled_instance, "bri": bri_seg1_wled_instance_1, "col": [rgb_seg1_wled_instance_1], "fx": effect_seg1_wled_instance_1}
        payload_seg2_wled_instance_1 = {"start": seg2start_wled_instance, "stop": seg2stop_wled_instance, "bri": bri_seg2_wled_instance_1, "col": [rgb_seg2_wled_instance_1], "fx": effect_seg2_wled_instance_1}
        payload_seg3_wled_instance_1 = {"start": seg3start_wled_instance, "stop": seg3stop_wled_instance, "bri": bri_seg3_wled_instance_1, "col": [rgb_seg3_wled_instance_1], "fx": effect_seg3_wled_instance_1}
        payload_seg4_wled_instance_1 = {"start": seg4start_wled_instance, "stop": seg4stop_wled_instance, "bri": bri_seg4_wled_instance_1, "col": [rgb_seg4_wled_instance_1], "fx": effect_seg4_wled_instance_1}
        payload_seg5_wled_instance_1 = {"start": seg5start_wled_instance, "stop": seg5stop_wled_instance, "bri": bri_seg5_wled_instance_1, "col": [rgb_seg5_wled_instance_1], "fx": effect_seg5_wled_instance_1}
        payload_seg6_wled_instance_1 = {"start": seg6start_wled_instance, "stop": seg6stop_wled_instance, "bri": bri_seg6_wled_instance_1, "col": [rgb_seg6_wled_instance_1], "fx": effect_seg6_wled_instance_1}
        payload_seg7_wled_instance_1 = {"start": seg7start_wled_instance, "stop": seg7stop_wled_instance, "bri": bri_seg7_wled_instance_1, "col": [rgb_seg7_wled_instance_1], "fx": effect_seg7_wled_instance_1}
        payload_seg8_wled_instance_1 = {"start": seg8start_wled_instance, "stop": seg8stop_wled_instance, "bri": bri_seg8_wled_instance_1, "col": [rgb_seg8_wled_instance_1], "fx": effect_seg8_wled_instance_1}
        payload_seg9_wled_instance_1 = {"start": seg9start_wled_instance, "stop": seg9stop_wled_instance, "bri": bri_seg9_wled_instance_1, "col": [rgb_seg9_wled_instance_1], "fx": effect_seg9_wled_instance_1}

        payload_wled_instance_1 = {"on": state, "bri": bri, "v": debugOutput,
                                  "seg": [payload_seg1_wled_instance_1, payload_seg2_wled_instance_1,
                                          payload_seg3_wled_instance_1, payload_seg4_wled_instance_1,
                                          payload_seg5_wled_instance_1, payload_seg6_wled_instance_1,
                                          payload_seg7_wled_instance_1, payload_seg8_wled_instance_1,
                                          payload_seg9_wled_instance_1]}

        #preparing payload json post to send to wled_instance_2:
        payload_seg1_wled_instance_2 = {"start": seg1start_wled_instance, "stop": seg1stop_wled_instance, "bri": bri_seg1_wled_instance_2, "col": [rgb_seg1_wled_instance_2], "fx": effect_seg1_wled_instance_2}
        payload_seg2_wled_instance_2 = {"start": seg2start_wled_instance, "stop": seg2stop_wled_instance, "bri": bri_seg2_wled_instance_2, "col": [rgb_seg2_wled_instance_2], "fx": effect_seg2_wled_instance_2}
        payload_seg3_wled_instance_2 = {"start": seg3start_wled_instance, "stop": seg3stop_wled_instance, "bri": bri_seg3_wled_instance_2, "col": [rgb_seg3_wled_instance_2], "fx": effect_seg3_wled_instance_2}
        payload_seg4_wled_instance_2 = {"start": seg4start_wled_instance, "stop": seg4stop_wled_instance, "bri": bri_seg4_wled_instance_2, "col": [rgb_seg4_wled_instance_2], "fx": effect_seg4_wled_instance_2}
        payload_seg5_wled_instance_2 = {"start": seg5start_wled_instance, "stop": seg5stop_wled_instance, "bri": bri_seg5_wled_instance_2, "col": [rgb_seg5_wled_instance_2], "fx": effect_seg5_wled_instance_2}
        payload_seg6_wled_instance_2 = {"start": seg6start_wled_instance, "stop": seg6stop_wled_instance, "bri": bri_seg6_wled_instance_2, "col": [rgb_seg6_wled_instance_2], "fx": effect_seg6_wled_instance_2}
        payload_seg7_wled_instance_2 = {"start": seg7start_wled_instance, "stop": seg7stop_wled_instance, "bri": bri_seg7_wled_instance_2, "col": [rgb_seg7_wled_instance_2], "fx": effect_seg7_wled_instance_2}
        payload_seg8_wled_instance_2 = {"start": seg8start_wled_instance, "stop": seg8stop_wled_instance, "bri": bri_seg8_wled_instance_2, "col": [rgb_seg8_wled_instance_2], "fx": effect_seg8_wled_instance_2}
        payload_seg9_wled_instance_2 = {"start": seg9start_wled_instance, "stop": seg9stop_wled_instance, "bri": bri_seg9_wled_instance_2, "col": [rgb_seg9_wled_instance_2], "fx": effect_seg9_wled_instance_2}

        payload_wled_instance_2 = {"on": state, "bri": bri, "v": debugOutput,
                                  "seg": [payload_seg1_wled_instance_2, payload_seg2_wled_instance_2,
                                          payload_seg3_wled_instance_2, payload_seg4_wled_instance_2,
                                          payload_seg5_wled_instance_2, payload_seg6_wled_instance_2,
                                          payload_seg7_wled_instance_2, payload_seg8_wled_instance_2,
                                          payload_seg9_wled_instance_2]}

        #preparing payload json post to send to wled_instance_3:
        payload_seg1_wled_instance_3 = {"start": seg1start_wled_instance, "stop": seg1stop_wled_instance, "bri": bri_seg1_wled_instance_3, "col": [rgb_seg1_wled_instance_3], "fx": effect_seg1_wled_instance_3}
        payload_seg2_wled_instance_3 = {"start": seg2start_wled_instance, "stop": seg2stop_wled_instance, "bri": bri_seg2_wled_instance_3, "col": [rgb_seg2_wled_instance_3], "fx": effect_seg2_wled_instance_3}
        payload_seg3_wled_instance_3 = {"start": seg3start_wled_instance, "stop": seg3stop_wled_instance, "bri": bri_seg3_wled_instance_3, "col": [rgb_seg3_wled_instance_3], "fx": effect_seg3_wled_instance_3}
        payload_seg4_wled_instance_3 = {"start": seg4start_wled_instance, "stop": seg4stop_wled_instance, "bri": bri_seg4_wled_instance_3, "col": [rgb_seg4_wled_instance_3], "fx": effect_seg4_wled_instance_3}
        payload_seg5_wled_instance_3 = {"start": seg5start_wled_instance, "stop": seg5stop_wled_instance, "bri": bri_seg5_wled_instance_3, "col": [rgb_seg5_wled_instance_3], "fx": effect_seg5_wled_instance_3}
        payload_seg6_wled_instance_3 = {"start": seg6start_wled_instance, "stop": seg6stop_wled_instance, "bri": bri_seg6_wled_instance_3, "col": [rgb_seg6_wled_instance_3], "fx": effect_seg6_wled_instance_3}
        payload_seg7_wled_instance_3 = {"start": seg7start_wled_instance, "stop": seg7stop_wled_instance, "bri": bri_seg7_wled_instance_3, "col": [rgb_seg7_wled_instance_3], "fx": effect_seg7_wled_instance_3}
        payload_seg8_wled_instance_3 = {"start": seg8start_wled_instance, "stop": seg8stop_wled_instance, "bri": bri_seg8_wled_instance_3, "col": [rgb_seg8_wled_instance_3], "fx": effect_seg8_wled_instance_3}
        payload_seg9_wled_instance_3 = {"start": seg9start_wled_instance, "stop": seg9stop_wled_instance, "bri": bri_seg9_wled_instance_3, "col": [rgb_seg9_wled_instance_3], "fx": effect_seg9_wled_instance_3}

        payload_wled_instance_3 = {"on": state, "bri": bri, "v": debugOutput,
                                  "seg": [payload_seg1_wled_instance_3, payload_seg2_wled_instance_3,
                                          payload_seg3_wled_instance_3, payload_seg4_wled_instance_3,
                                          payload_seg5_wled_instance_3, payload_seg6_wled_instance_3,
                                          payload_seg7_wled_instance_3, payload_seg8_wled_instance_3,
                                          payload_seg9_wled_instance_3]}

        #preparing payload json post to send to wled_instance_4:
        payload_seg1_wled_instance_4 = {"start": seg1start_wled_instance, "stop": seg1stop_wled_instance, "bri": bri_seg1_wled_instance_4, "col": [rgb_seg1_wled_instance_4], "fx": effect_seg1_wled_instance_4}
        payload_seg2_wled_instance_4 = {"start": seg2start_wled_instance, "stop": seg2stop_wled_instance, "bri": bri_seg2_wled_instance_4, "col": [rgb_seg2_wled_instance_4], "fx": effect_seg2_wled_instance_4}
        payload_seg3_wled_instance_4 = {"start": seg3start_wled_instance, "stop": seg3stop_wled_instance, "bri": bri_seg3_wled_instance_4, "col": [rgb_seg3_wled_instance_4], "fx": effect_seg3_wled_instance_4}
        payload_seg4_wled_instance_4 = {"start": seg4start_wled_instance, "stop": seg4stop_wled_instance, "bri": bri_seg4_wled_instance_4, "col": [rgb_seg4_wled_instance_4], "fx": effect_seg4_wled_instance_4}
        payload_seg5_wled_instance_4 = {"start": seg5start_wled_instance, "stop": seg5stop_wled_instance, "bri": bri_seg5_wled_instance_4, "col": [rgb_seg5_wled_instance_4], "fx": effect_seg5_wled_instance_4}
        payload_seg6_wled_instance_4 = {"start": seg6start_wled_instance, "stop": seg6stop_wled_instance, "bri": bri_seg6_wled_instance_4, "col": [rgb_seg6_wled_instance_4], "fx": effect_seg6_wled_instance_4}
        payload_seg7_wled_instance_4 = {"start": seg7start_wled_instance, "stop": seg7stop_wled_instance, "bri": bri_seg7_wled_instance_4, "col": [rgb_seg7_wled_instance_4], "fx": effect_seg7_wled_instance_4}
        payload_seg8_wled_instance_4 = {"start": seg8start_wled_instance, "stop": seg8stop_wled_instance, "bri": bri_seg8_wled_instance_4, "col": [rgb_seg8_wled_instance_4], "fx": effect_seg8_wled_instance_4}
        payload_seg9_wled_instance_4 = {"start": seg9start_wled_instance, "stop": seg9stop_wled_instance, "bri": bri_seg9_wled_instance_4, "col": [rgb_seg9_wled_instance_4], "fx": effect_seg9_wled_instance_4}

        payload_wled_instance_4 = {"on": state, "bri": bri, "v": debugOutput,
                                  "seg": [payload_seg1_wled_instance_4, payload_seg2_wled_instance_4,
                                          payload_seg3_wled_instance_4, payload_seg4_wled_instance_4,
                                          payload_seg5_wled_instance_4, payload_seg6_wled_instance_4,
                                          payload_seg7_wled_instance_4, payload_seg8_wled_instance_4,
                                          payload_seg9_wled_instance_4]}

        #preparing payload json post to send to wled_instance_5:
        payload_seg1_wled_instance_5 = {"start": seg1start_wled_instance, "stop": seg1stop_wled_instance, "bri": bri_seg1_wled_instance_5, "col": [rgb_seg1_wled_instance_5], "fx": effect_seg1_wled_instance_5}
        payload_seg2_wled_instance_5 = {"start": seg2start_wled_instance, "stop": seg2stop_wled_instance, "bri": bri_seg2_wled_instance_5, "col": [rgb_seg2_wled_instance_5], "fx": effect_seg2_wled_instance_5}
        payload_seg3_wled_instance_5 = {"start": seg3start_wled_instance, "stop": seg3stop_wled_instance, "bri": bri_seg3_wled_instance_5, "col": [rgb_seg3_wled_instance_5], "fx": effect_seg3_wled_instance_5}
        payload_seg4_wled_instance_5 = {"start": seg4start_wled_instance, "stop": seg4stop_wled_instance, "bri": bri_seg4_wled_instance_5, "col": [rgb_seg4_wled_instance_5], "fx": effect_seg4_wled_instance_5}
        payload_seg5_wled_instance_5 = {"start": seg5start_wled_instance, "stop": seg5stop_wled_instance, "bri": bri_seg5_wled_instance_5, "col": [rgb_seg5_wled_instance_5], "fx": effect_seg5_wled_instance_5}
        payload_seg6_wled_instance_5 = {"start": seg6start_wled_instance, "stop": seg6stop_wled_instance, "bri": bri_seg6_wled_instance_5, "col": [rgb_seg6_wled_instance_5], "fx": effect_seg6_wled_instance_5}
        payload_seg7_wled_instance_5 = {"start": seg7start_wled_instance, "stop": seg7stop_wled_instance, "bri": bri_seg7_wled_instance_5, "col": [rgb_seg7_wled_instance_5], "fx": effect_seg7_wled_instance_5}
        payload_seg8_wled_instance_5 = {"start": seg8start_wled_instance, "stop": seg8stop_wled_instance, "bri": bri_seg8_wled_instance_5, "col": [rgb_seg8_wled_instance_5], "fx": effect_seg8_wled_instance_5}
        payload_seg9_wled_instance_5 = {"start": seg9start_wled_instance, "stop": seg9stop_wled_instance, "bri": bri_seg9_wled_instance_5, "col": [rgb_seg9_wled_instance_5], "fx": effect_seg9_wled_instance_5}

        payload_wled_instance_5 = {"on": state, "bri": bri, "v": debugOutput,
                                  "seg": [payload_seg1_wled_instance_5, payload_seg2_wled_instance_5,
                                          payload_seg3_wled_instance_5, payload_seg4_wled_instance_5,
                                          payload_seg5_wled_instance_5, payload_seg6_wled_instance_5,
                                          payload_seg7_wled_instance_5, payload_seg8_wled_instance_5,
                                          payload_seg9_wled_instance_5]}

        #preparing payload json post to send to wled_instance_6:
        payload_seg1_wled_instance_6 = {"start": seg1start_wled_instance, "stop": seg1stop_wled_instance, "bri": bri_seg1_wled_instance_6, "col": [rgb_seg1_wled_instance_6], "fx": effect_seg1_wled_instance_6}
        payload_seg2_wled_instance_6 = {"start": seg2start_wled_instance, "stop": seg2stop_wled_instance, "bri": bri_seg2_wled_instance_6, "col": [rgb_seg2_wled_instance_6], "fx": effect_seg2_wled_instance_6}
        payload_seg3_wled_instance_6 = {"start": seg3start_wled_instance, "stop": seg3stop_wled_instance, "bri": bri_seg3_wled_instance_6, "col": [rgb_seg3_wled_instance_6], "fx": effect_seg3_wled_instance_6}
        payload_seg4_wled_instance_6 = {"start": seg4start_wled_instance, "stop": seg4stop_wled_instance, "bri": bri_seg4_wled_instance_6, "col": [rgb_seg4_wled_instance_6], "fx": effect_seg4_wled_instance_6}
        payload_seg5_wled_instance_6 = {"start": seg5start_wled_instance, "stop": seg5stop_wled_instance, "bri": bri_seg5_wled_instance_6, "col": [rgb_seg5_wled_instance_6], "fx": effect_seg5_wled_instance_6}
        payload_seg6_wled_instance_6 = {"start": seg6start_wled_instance, "stop": seg6stop_wled_instance, "bri": bri_seg6_wled_instance_6, "col": [rgb_seg6_wled_instance_6], "fx": effect_seg6_wled_instance_6}
        payload_seg7_wled_instance_6 = {"start": seg7start_wled_instance, "stop": seg7stop_wled_instance, "bri": bri_seg7_wled_instance_6, "col": [rgb_seg7_wled_instance_6], "fx": effect_seg7_wled_instance_6}
        payload_seg8_wled_instance_6 = {"start": seg8start_wled_instance, "stop": seg8stop_wled_instance, "bri": bri_seg8_wled_instance_6, "col": [rgb_seg8_wled_instance_6], "fx": effect_seg8_wled_instance_6}
        payload_seg9_wled_instance_6 = {"start": seg9start_wled_instance, "stop": seg9stop_wled_instance, "bri": bri_seg9_wled_instance_6, "col": [rgb_seg9_wled_instance_6], "fx": effect_seg9_wled_instance_6}

        payload_wled_instance_6 = {"on": state, "bri": bri, "v": debugOutput,
                                  "seg": [payload_seg1_wled_instance_6, payload_seg2_wled_instance_6,
                                          payload_seg3_wled_instance_6, payload_seg4_wled_instance_6,
                                          payload_seg5_wled_instance_6, payload_seg6_wled_instance_6,
                                          payload_seg7_wled_instance_6, payload_seg8_wled_instance_6,
                                          payload_seg9_wled_instance_6]}

        # preparing payload json post to send to wled_controll_unit_instance:
        payload_wled_controll_unit_instance = {"on": state, "bri": bri, "v": debugOutput,
                                  "seg": [{"start": 0, "stop": 12, "bri": PotBrightness, "col": [pot_rgb], "fx": enc_effect}]}


        print("payloads were prepared...")

        # sending payload to wled_controll_unit_instance
        headers = {'content-type': 'application/json'}
        request_wled_controll_unit_instance = requests.post(wled_controll_unit_instance, data=json.dumps(payload_wled_controll_unit_instance), headers=headers, timeout=5)
        print("wled_controll_unit_instance responded with: ", request_wled_controll_unit_instance.status_code, request_wled_controll_unit_instance.json())
        print()


        #sending payload to wled_instance_1
        headers ={'content-type':'application/json'}
        request_wled_instance_1 = requests.post(wled_instance_1, data=json.dumps(payload_wled_instance_1),headers=headers, timeout=5 )
        print("wled_instance_1 responded with: ",request_wled_instance_1.status_code, request_wled_instance_1.json())
        print()

        #sending payload to wled_instance_2
        headers ={'content-type':'application/json'}
        request_wled_instance_2 = requests.post(wled_instance_2, data=json.dumps(payload_wled_instance_2),headers=headers, timeout=5 )
        print("wled_instance_2 responded with: ",request_wled_instance_2.status_code, request_wled_instance_2.json())
        print()

        #sending payload to wled_instance_3
        headers ={'content-type':'application/json'}
        request_wled_instance_3 = requests.post(wled_instance_3, data=json.dumps(payload_wled_instance_3),headers=headers, timeout=5 )
        print("wled_instance_3 responded with: ",request_wled_instance_3.status_code, request_wled_instance_3.json())
        print()

        #sending payload to wled_instance_4
        headers ={'content-type':'application/json'}
        request_wled_instance_4 = requests.post(wled_instance_4, data=json.dumps(payload_wled_instance_4),headers=headers, timeout=5 )
        print("wled_instance_4 responded with: ",request_wled_instance_4.status_code, request_wled_instance_4.json())
        print()

        #sending payload to wled_instance_5
        headers ={'content-type':'application/json'}
        request_wled_instance_5 = requests.post(wled_instance_5, data=json.dumps(payload_wled_instance_5),headers=headers, timeout=5 )
        print("wled_instance_5 responded with: ",request_wled_instance_5.status_code, request_wled_instance_5.json())
        print()

        #sending payload to wled_instance_6
        headers ={'content-type':'application/json'}
        request_wled_instance_6 = requests.post(wled_instance_6, data=json.dumps(payload_wled_instance_6),headers=headers, timeout=5 )
        print("wled_instance_6 responded with: ",request_wled_instance_6.status_code, request_wled_instance_6.json())
        print()

    except Exception:
        pass




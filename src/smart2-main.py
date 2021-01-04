import smart2


if __name__ == '__main__':

    smart2 = smart2.Smart2()

    # while True:
    for i in range(10):
        val = smart2.capture_audio()
        if val:
            smart2.analyze_audio(val)

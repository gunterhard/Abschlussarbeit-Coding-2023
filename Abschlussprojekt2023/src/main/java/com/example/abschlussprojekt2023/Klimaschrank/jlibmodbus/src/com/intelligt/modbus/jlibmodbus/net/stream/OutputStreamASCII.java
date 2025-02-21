package com.example.abschlussprojekt2023.Klimaschrank.jlibmodbus.src.com.intelligt.modbus.jlibmodbus.net.stream;

import com.example.abschlussprojekt2023.Klimaschrank.jlibmodbus.src.com.intelligt.modbus.jlibmodbus.Modbus;
import com.example.abschlussprojekt2023.Klimaschrank.jlibmodbus.src.com.intelligt.modbus.jlibmodbus.serial.SerialPort;
import com.example.abschlussprojekt2023.Klimaschrank.jlibmodbus.src.com.intelligt.modbus.jlibmodbus.utils.DataUtils;

import java.io.IOException;
import java.nio.charset.Charset;

/*
 * Copyright (C) 2016 "Invertor" Factory", JSC
 * [http://www.sbp-invertor.ru]
 *
 * This file is part of JLibModbus.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *  http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 * Authors: Vladislav Y. Kochedykov, software engineer.
 * email: vladislav.kochedykov@gmail.com
 */
public class OutputStreamASCII extends OutputStreamSerial {

    private int lrc = 0;

    public OutputStreamASCII(SerialPort serial) {
        super(serial);
        reset();
    }

    @Override
    public void write(byte[] bytes) throws IOException {
        write(bytes, 0, bytes.length);
    }

    @Override
    public void write(byte[] bytes, int offset, int length) throws IOException {
        int tail = offset+length;
        for (int i = offset; i < tail; i++) {
            lrc += bytes[i];
        }
        byte[] ascii = DataUtils.toAscii(bytes, offset, length).getBytes(Charset.forName("ASCII"));
        super.write(ascii);
    }

    @Override
    public void write(int b) throws IOException {
        lrc += (byte) b;
        byte[] bytes = DataUtils.toAscii((byte) b).getBytes(Charset.forName("ASCII"));
        super.write(bytes);
    }

    public void writeRaw(int b) throws IOException {
        super.write(b);
    }

    @Override
    public void flush() throws IOException {
        writeChecksum();
        writeRaw(Modbus.ASCII_CODE_CR);
        writeRaw(Modbus.ASCII_CODE_LF);
        super.flush();
        reset();
    }

    public void reset() {
        try {
            lrc = 0;
            writeRaw(Modbus.ASCII_CODE_COLON);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private void writeChecksum() throws IOException {
        byte[] bytes = DataUtils.toAscii((byte) -lrc).getBytes(Charset.forName("ASCII"));
        super.write(bytes);
    }
}

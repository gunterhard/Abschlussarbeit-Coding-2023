package com.example.abschlussprojekt2023.Klimaschrank.jlibmodbus.src.com.intelligt.modbus.jlibmodbus.msg.base.mei;

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
public enum ReadDeviceIdentificationCode {
    BASIC_STREAM_ACCESS(0x01),
    REGULAR_STREAM_ACCESS(0x02),
    EXTENDED_STREAM_ACCESS(0x03),
    ONE_SPECIFIC_INDIVIDUAL_ACCESS(0x04);

    final private int code;

    ReadDeviceIdentificationCode(int code) {
        this.code = code;
    }

    static public ReadDeviceIdentificationCode get(int code) {
        for (ReadDeviceIdentificationCode c : values()) {
            if (c.toInt() == code) {
                return c;
            }
        }
        return BASIC_STREAM_ACCESS;
    }

    public int toInt() {
        return code;
    }
}

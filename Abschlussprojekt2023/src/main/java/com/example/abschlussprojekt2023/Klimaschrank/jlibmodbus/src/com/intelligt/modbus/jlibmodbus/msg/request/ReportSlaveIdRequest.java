package com.example.abschlussprojekt2023.Klimaschrank.jlibmodbus.src.com.intelligt.modbus.jlibmodbus.msg.request;

import com.example.abschlussprojekt2023.Klimaschrank.jlibmodbus.src.com.intelligt.modbus.jlibmodbus.data.DataHolder;
import com.example.abschlussprojekt2023.Klimaschrank.jlibmodbus.src.com.intelligt.modbus.jlibmodbus.exception.ModbusNumberException;
import com.example.abschlussprojekt2023.Klimaschrank.jlibmodbus.src.com.intelligt.modbus.jlibmodbus.exception.ModbusProtocolException;
import com.example.abschlussprojekt2023.Klimaschrank.jlibmodbus.src.com.intelligt.modbus.jlibmodbus.msg.base.ModbusRequest;
import com.example.abschlussprojekt2023.Klimaschrank.jlibmodbus.src.com.intelligt.modbus.jlibmodbus.msg.base.ModbusResponse;
import com.example.abschlussprojekt2023.Klimaschrank.jlibmodbus.src.com.intelligt.modbus.jlibmodbus.msg.response.ReportSlaveIdResponse;
import com.example.abschlussprojekt2023.Klimaschrank.jlibmodbus.src.com.intelligt.modbus.jlibmodbus.net.stream.base.ModbusInputStream;
import com.example.abschlussprojekt2023.Klimaschrank.jlibmodbus.src.com.intelligt.modbus.jlibmodbus.net.stream.base.ModbusOutputStream;
import com.example.abschlussprojekt2023.Klimaschrank.jlibmodbus.src.com.intelligt.modbus.jlibmodbus.utils.ModbusFunctionCode;

import java.io.IOException;

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
final public class ReportSlaveIdRequest extends ModbusRequest {

    public ReportSlaveIdRequest() {
        super();
    }

    @Override
    protected Class getResponseClass() {
        return ReportSlaveIdResponse.class;
    }

    @Override
    public void writeRequest(ModbusOutputStream fifo) throws IOException {
        //no operation
    }

    @Override
    public int requestSize() {
        return 0;
    }

    @Override
    public ModbusResponse process(DataHolder dataHolder) throws ModbusNumberException {
        ReportSlaveIdResponse response = (ReportSlaveIdResponse) getResponse();
        try {
            byte[] slaveId = dataHolder.readSlaveId();
            response.setSlaveId(slaveId);
        } catch (ModbusProtocolException e) {
            response.setException();
            response.setModbusExceptionCode(e.getException().getValue());
        }
        return response;
    }

    @Override
    public boolean validateResponseImpl(ModbusResponse response) {
        return true;
    }

    @Override
    public void readPDU(ModbusInputStream fifo) throws ModbusNumberException, IOException {
        //no operation
    }

    @Override
    public int getFunction() {
        return ModbusFunctionCode.REPORT_SLAVE_ID.toInt();
    }
}

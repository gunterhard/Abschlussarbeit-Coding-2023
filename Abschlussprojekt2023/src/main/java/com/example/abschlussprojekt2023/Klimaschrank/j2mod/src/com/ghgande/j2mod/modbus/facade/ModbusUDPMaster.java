//License
/***
 * Java Modbus Library (jamod)
 * Copyright (c) 2002-2004, jamod development team
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are
 * met:
 *
 * Redistributions of source code must retain the above copyright notice,
 * this list of conditions and the following disclaimer.
 *
 * Redistributions in binary form must reproduce the above copyright notice,
 * this list of conditions and the following disclaimer in the documentation
 * and/or other materials provided with the distribution.
 *
 * Neither the name of the author nor the names of its contributors
 * may be used to endorse or promote products derived from this software
 * without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDER AND CONTRIBUTORS ``AS
 * IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
 * THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
 * PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 ***/
package com.example.abschlussprojekt2023.Klimaschrank.j2mod.src.com.ghgande.j2mod.modbus.facade;


import java.net.InetAddress;
import java.net.UnknownHostException;

import com.example.abschlussprojekt2023.Klimaschrank.j2mod.src.com.ghgande.j2mod.modbus.ModbusException;
import com.example.abschlussprojekt2023.Klimaschrank.j2mod.src.com.ghgande.j2mod.modbus.io.ModbusUDPTransaction;
import com.example.abschlussprojekt2023.Klimaschrank.j2mod.src.com.ghgande.j2mod.modbus.msg.*;
import com.example.abschlussprojekt2023.Klimaschrank.j2mod.src.com.ghgande.j2mod.modbus.net.UDPMasterConnection;
import com.example.abschlussprojekt2023.Klimaschrank.j2mod.src.com.ghgande.j2mod.modbus.procimg.InputRegister;
import com.example.abschlussprojekt2023.Klimaschrank.j2mod.src.com.ghgande.j2mod.modbus.procimg.Register;
import com.example.abschlussprojekt2023.Klimaschrank.j2mod.src.com.ghgande.j2mod.modbus.util.BitVector;

/**
 * Modbus/UDP Master facade.
 *
 * @author Dieter Wimberger
 * @version 1.2rc1 (09/11/2004)
 */
public class ModbusUDPMaster {

  private UDPMasterConnection m_Connection;
  private InetAddress m_SlaveAddress;
  private ModbusUDPTransaction m_Transaction;
  private ReadCoilsRequest m_ReadCoilsRequest;
  private ReadInputDiscretesRequest m_ReadInputDiscretesRequest;
  private WriteCoilRequest m_WriteCoilRequest;
  private WriteMultipleCoilsRequest m_WriteMultipleCoilsRequest;
  private ReadInputRegistersRequest m_ReadInputRegistersRequest;
  private ReadMultipleRegistersRequest m_ReadMultipleRegistersRequest;
  private WriteSingleRegisterRequest m_WriteSingleRegisterRequest;
  private WriteMultipleRegistersRequest m_WriteMultipleRegistersRequest;

  /**
   * Constructs a new master facade instance for communication
   * with a given slave.
   *
   * @param addr an internet address as resolvable IP name or IP number,
   *             specifying the slave to communicate with.
   */
  public ModbusUDPMaster(String addr) {
    try {
      m_SlaveAddress = InetAddress.getByName(addr);
      m_Connection = new UDPMasterConnection(m_SlaveAddress);
      m_ReadCoilsRequest = new ReadCoilsRequest();
      m_ReadInputDiscretesRequest = new ReadInputDiscretesRequest();
      m_WriteCoilRequest = new WriteCoilRequest();
      m_WriteMultipleCoilsRequest = new WriteMultipleCoilsRequest();
      m_ReadInputRegistersRequest = new ReadInputRegistersRequest();
      m_ReadMultipleRegistersRequest = new ReadMultipleRegistersRequest();
      m_WriteSingleRegisterRequest = new WriteSingleRegisterRequest();
      m_WriteMultipleRegistersRequest = new WriteMultipleRegistersRequest();

    } catch (UnknownHostException e) {
      throw new RuntimeException(e.getMessage());
    }
  }//constructor

  /**
   * Constructs a new master facade instance for communication
   * with a given slave.
   *
   * @param addr an internet address as resolvable IP name or IP number,
   *             specifying the slave to communicate with.
   * @param port the port the slave is listening to.
   */
  public ModbusUDPMaster(String addr, int port) {
    this(addr);
    m_Connection.setPort(port);
  }//constructor

  /**
   * Connects this <tt>ModbusUDPMaster</tt> with the slave.
   *
   * @throws Exception if the connection cannot be established.
   */
  public void connect()
      throws Exception {
    if (m_Connection != null && !m_Connection.isConnected()) {
      m_Connection.connect();
      m_Transaction = new ModbusUDPTransaction(m_Connection);
    }
  }//connect

  /**
   * Disconnects this <tt>ModbusTCPMaster</tt> from the slave.
   */
  public void disconnect() {
    if (m_Connection != null && m_Connection.isConnected()) {
      m_Connection.close();
      m_Transaction = null;
    }
  }//disconnect

  /**
   * Reads a given number of coil states from the slave.
   * <p/>
   * Note that the number of bits in the bit vector will be
   * forced to the number originally requested.
   *
   * @param ref   the offset of the coil to start reading from.
   * @param count the number of coil states to be read.
   * @return a <tt>BitVector</tt> instance holding the
   *         received coil states.
   * @throws ModbusException if an I/O error, a slave exception or
   *                         a transaction error occurs.
   */
  public synchronized BitVector readCoils(int ref, int count)
      throws ModbusException {
    m_ReadCoilsRequest.setReference(ref);
    m_ReadCoilsRequest.setBitCount(count);
    m_Transaction.setRequest(m_ReadCoilsRequest);
    m_Transaction.execute();
    BitVector bv = ((ReadCoilsResponse) m_Transaction.getResponse()).getCoils();
    bv.forceSize(count);
    return bv;
  }//readCoils

  /**
   * Writes a coil state to the slave.
   *
   * @param unitid the slave unit id.
   * @param ref    the offset of the coil to be written.
   * @param state  the coil state to be written.
   * @return the state of the coil as returned from the slave.
   * @throws ModbusException if an I/O error, a slave exception or
   *                         a transaction error occurs.
   */
  public synchronized boolean writeCoil(int unitid, int ref, boolean state)
      throws ModbusException {
    m_WriteCoilRequest.setUnitID(unitid);
    m_WriteCoilRequest.setReference(ref);
    m_WriteCoilRequest.setCoil(state);
    m_Transaction.setRequest(m_WriteCoilRequest);
    m_Transaction.execute();
    return ((WriteCoilResponse) m_Transaction.getResponse()).getCoil();
  }//writeCoil

  /**
   * Writes a given number of coil states to the slave.
   * <p/>
   * Note that the number of coils to be written is given
   * implicitly, through {@link BitVector#size()}.
   *
   * @param ref   the offset of the coil to start writing to.
   * @param coils a <tt>BitVector</tt> which holds the coil states to be written.
   * @throws ModbusException if an I/O error, a slave exception or
   *                         a transaction error occurs.
   */
  public synchronized void writeMultipleCoils(int ref, BitVector coils)
      throws ModbusException {
    m_WriteMultipleCoilsRequest.setReference(ref);
    m_WriteMultipleCoilsRequest.setCoils(coils);
    m_Transaction.setRequest(m_WriteMultipleCoilsRequest);
    m_Transaction.execute();
  }//writeMultipleCoils

  /**
   * Reads a given number of input discrete states from the slave.
   * <p/>
   * Note that the number of bits in the bit vector will be
   * forced to the number originally requested.
   *
   * @param ref   the offset of the input discrete to start reading from.
   * @param count the number of input discrete states to be read.
   * @return a <tt>BitVector</tt> instance holding the received input discrete
   *         states.
   * @throws ModbusException if an I/O error, a slave exception or
   *                         a transaction error occurs.
   */
  public synchronized BitVector readInputDiscretes(int ref, int count)
      throws ModbusException {
    m_ReadInputDiscretesRequest.setReference(ref);
    m_ReadInputDiscretesRequest.setBitCount(count);
    m_Transaction.setRequest(m_ReadInputDiscretesRequest);
    m_Transaction.execute();
    BitVector bv = ((ReadInputDiscretesResponse) m_Transaction.getResponse()).getDiscretes();
    bv.forceSize(count);
    return bv;
  }//readInputDiscretes


  /**
   * Reads a given number of input registers from the slave.
   * <p/>
   * Note that the number of input registers returned (i.e. array length)
   * will be according to the number received in the slave response.
   *
   * @param ref   the offset of the input register to start reading from.
   * @param count the number of input registers to be read.
   * @return a <tt>InputRegister[]</tt> with the received input registers.
   * @throws ModbusException if an I/O error, a slave exception or
   *                         a transaction error occurs.
   */
  public synchronized InputRegister[] readInputRegisters(int ref, int count)
      throws ModbusException {
    m_ReadInputRegistersRequest.setReference(ref);
    m_ReadInputRegistersRequest.setWordCount(count);
    m_Transaction.setRequest(m_ReadInputRegistersRequest);
    m_Transaction.execute();
    return ((ReadInputRegistersResponse) m_Transaction.getResponse()).getRegisters();
  }//readInputRegisters

  /**
   * Reads a given number of registers from the slave.
   * <p/>
   * Note that the number of registers returned (i.e. array length)
   * will be according to the number received in the slave response.
   *
   * @param ref   the offset of the register to start reading from.
   * @param count the number of registers to be read.
   * @return a <tt>Register[]</tt> holding the received registers.
   * @throws ModbusException if an I/O error, a slave exception or
   *                         a transaction error occurs.
   */
  public synchronized Register[] readMultipleRegisters(int ref, int count)
      throws ModbusException {
    m_ReadMultipleRegistersRequest.setReference(ref);
    m_ReadMultipleRegistersRequest.setWordCount(count);
    m_Transaction.setRequest(m_ReadMultipleRegistersRequest);
    m_Transaction.execute();
    return ((ReadMultipleRegistersResponse) m_Transaction.getResponse()).getRegisters();
  }//readMultipleRegisters

  /**
   * Writes a single register to the slave.
   *
   * @param ref      the offset of the register to be written.
   * @param register a <tt>Register</tt> holding the value of the register
   *                 to be written.
   * @throws ModbusException if an I/O error, a slave exception or
   *                         a transaction error occurs.
   */
  public synchronized void writeSingleRegister(int ref, Register register)
      throws ModbusException {
    m_WriteSingleRegisterRequest.setReference(ref);
    m_WriteSingleRegisterRequest.setRegister(register);
    m_Transaction.setRequest(m_WriteSingleRegisterRequest);
    m_Transaction.execute();
  }//writeSingleRegister

  /**
   * Writes a number of registers to the slave.
   *
   * @param ref       the offset of the register to start writing to.
   * @param registers a <tt>Register[]</tt> holding the values of
   *                  the registers to be written.
   * @throws ModbusException if an I/O error, a slave exception or
   *                         a transaction error occurs.
   */
  public synchronized void writeMultipleRegisters(int ref, Register[] registers)
      throws ModbusException {
    m_WriteMultipleRegistersRequest.setReference(ref);
    m_WriteMultipleRegistersRequest.setRegisters(registers);
    m_Transaction.setRequest(m_WriteMultipleRegistersRequest);
    m_Transaction.execute();
  }//writeMultipleRegisters

}//class ModbusUDPMaster

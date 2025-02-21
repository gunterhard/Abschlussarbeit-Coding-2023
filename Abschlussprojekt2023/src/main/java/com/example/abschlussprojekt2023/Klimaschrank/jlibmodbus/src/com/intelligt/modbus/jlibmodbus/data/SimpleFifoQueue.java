package com.example.abschlussprojekt2023.Klimaschrank.jlibmodbus.src.com.intelligt.modbus.jlibmodbus.data;

import com.example.abschlussprojekt2023.Klimaschrank.jlibmodbus.src.com.intelligt.modbus.jlibmodbus.Modbus;

import java.util.Iterator;
import java.util.LinkedList;
import java.util.Queue;

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
public class SimpleFifoQueue extends FifoQueue {

    final private Queue<Integer> queue = new LinkedList<Integer>();

    public SimpleFifoQueue() {
        super(Modbus.MAX_FIFO_COUNT);
    }

    @Override
    public int size() {
        return queue.size();
    }

    @Override
    protected int[] peekImpl() {
        if (queue.size() > 0) {
            int[] r = new int[queue.size()];
            Iterator<Integer> iterator = queue.iterator();
            for (int i = 0; i < r.length && iterator.hasNext(); i++) {
                r[i] = iterator.next();
            }
            return r;
        }
        return new int[0];
    }

    @Override
    protected void addImpl(int register) {
        queue.add(register);
    }

    @Override
    protected void pollImpl() {
        queue.poll();
    }
}

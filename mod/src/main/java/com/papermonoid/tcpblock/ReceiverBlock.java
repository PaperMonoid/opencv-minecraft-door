package com.papermonoid.tcpblock;

import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Random;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import net.minecraft.block.Block;
import net.minecraft.block.BlockState;
import net.minecraft.block.Blocks;
import net.minecraft.tileentity.TileEntity;
import net.minecraft.util.Direction;
import net.minecraft.util.math.BlockPos;
import net.minecraft.world.IBlockReader;

public class ReceiverBlock extends Block {
	
	public static class Receiver extends Thread {
		
		public boolean isTrue;
		private Socket socket;
		private InputStreamReader reader;
		
		private static Receiver instance;
		
		private Receiver() {
			isTrue = false;
			socket = null;
			reader = null;
		}
		
		@Override
		public void run() {
			while (true) {
				try {
					update();
					sleep(100);
				} catch (InterruptedException e) {
					e.printStackTrace();
				} catch (IOException e) {
					e.printStackTrace();
				} 
			}
		}
		
		synchronized private void update() throws IOException {
			if (reader != null)
				isTrue = reader.read() == '1';
		}
		
		public static Receiver getInstance() {
			if (instance == null) {
				instance = new Receiver();
				instance.start();
			}
			return instance;
		}
		
		public void openConnection() throws UnknownHostException, IOException {
			if (socket == null && reader == null) {
				socket = new Socket("localhost", 1069);
				reader = new InputStreamReader(socket.getInputStream());
			}
		}
		
		public void closeConnection() throws IOException {
			if (socket != null && reader != null) {
				socket.close();
				reader.close();
				socket = null;
				reader = null;
			}
		}
		
	}

	public ReceiverBlock() {
		super(Block.Properties.from(Blocks.REDSTONE_BLOCK));
		setRegistryName("receiver_block");
	}
    
	@Override
	public int getWeakPower(BlockState blockState, IBlockReader blockAccess, BlockPos pos, Direction side) {
		return Receiver.getInstance().isTrue ? 15 : 0;
	}

    @Override
    public boolean hasTileEntity(BlockState state) {
        return true;
    }
    
    @Override
    public TileEntity createTileEntity(BlockState state, IBlockReader world) {
        return new ReceiverTile();
    }

	@Override
	public boolean canConnectRedstone(BlockState state, IBlockReader world, BlockPos pos, Direction side) {
		return true;
	}

	@Override
	public boolean canProvidePower(BlockState state) {
		return true;
	}

}

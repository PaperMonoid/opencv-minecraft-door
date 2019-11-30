package com.papermonoid.tcpblock;

import net.minecraft.tileentity.ITickableTileEntity;
import net.minecraft.tileentity.TileEntity;

public class ReceiverTile extends TileEntity implements ITickableTileEntity {
	
	private boolean isTrue;

	public ReceiverTile() {
		super(ModBlocks.RECEIVER_TILE);
		this.isTrue = false;
	}
	
	@Override
	public void tick() {
		if (this.isTrue != ReceiverBlock.Receiver.getInstance().isTrue) {
			this.isTrue = ReceiverBlock.Receiver.getInstance().isTrue;
			this.world.notifyNeighbors(this.pos, this.getBlockState().getBlock());
		}
	}

}

package com.papermonoid.tcpblock;

import net.minecraft.item.BlockItem;

public class ReceiverItem extends BlockItem {

	public ReceiverItem() {
		super(ModBlocks.RECEIVER_BLOCK, new Properties());
		setRegistryName("receiver_block");
	}

}

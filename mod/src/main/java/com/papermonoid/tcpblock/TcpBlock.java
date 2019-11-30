package com.papermonoid.tcpblock;

import net.minecraft.block.Block;
import net.minecraft.block.Blocks;
import net.minecraft.item.Item;
import net.minecraft.tileentity.TileEntityType;
import net.minecraftforge.common.MinecraftForge;
import net.minecraftforge.event.RegistryEvent;
import net.minecraftforge.event.world.WorldEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.event.lifecycle.FMLCommonSetupEvent;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;

import java.io.IOException;
import java.net.UnknownHostException;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

// The value here should match an entry in the META-INF/mods.toml file
@Mod("tcpblock")
public class TcpBlock
{
    private static final Logger LOGGER = LogManager.getLogger();

    public TcpBlock() {
        FMLJavaModLoadingContext.get().getModEventBus().addListener(this::setup);
        MinecraftForge.EVENT_BUS.register(this);
    }

    private void setup(final FMLCommonSetupEvent event) {
        LOGGER.info("HELLO FROM PREINIT");
        LOGGER.info("DIRT BLOCK >> {}", Blocks.DIRT.getRegistryName());
    }
    
    int openWorldCounter = 0;
    
    @SubscribeEvent
    public void onWorldLoad(WorldEvent.Load event) {
    	openWorldCounter++;
    	LOGGER.info("OPENING!!!!");
    	try {
			ReceiverBlock.Receiver.getInstance().openConnection();
		} catch (UnknownHostException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
    }
    
    @SubscribeEvent
    public void onWorldUnload(WorldEvent.Unload event) {
    	if (openWorldCounter > 3) {
    		openWorldCounter = 0;
	    	LOGGER.info("CLOSING!!!!");
	    	try {
				ReceiverBlock.Receiver.getInstance().closeConnection();
			} catch (IOException e) {
				e.printStackTrace();
			}
    	}
    }
    
    @Mod.EventBusSubscriber(bus=Mod.EventBusSubscriber.Bus.MOD)
    public static class RegistryEvents {
    	
    	@SubscribeEvent
    	public static void registerBlocks(RegistryEvent.Register<Block> event) {
    		event.getRegistry().registerAll(new ReceiverBlock());
    	}
    	
    	@SubscribeEvent
    	public static void registerItemBlocks(RegistryEvent.Register<Item> event) {
    		event.getRegistry().registerAll(new ReceiverItem());
    	}
    	
        @SubscribeEvent
        public static void onTileEntityRegistry(final RegistryEvent.Register<TileEntityType<?>> event) {
            event.getRegistry().register(TileEntityType.Builder.create(ReceiverTile::new, ModBlocks.RECEIVER_BLOCK)            		
            		.build(null)
            		.setRegistryName("receiver_block"));
        }
    	
        @SubscribeEvent
        public static void onBlocksRegistry(final RegistryEvent.Register<Block> blockRegistryEvent) {
            // register a new block here
            LOGGER.info("HELLO from Register Block");
        }
    }
}


#%%
# TheGraph Subgraph for Phase 2 - Current Phase
# TheGraph Subgraph for Phase 3 - Next Phase
#subgraph_phase2 = "https://api.thegraph.com/subgraphs/name/graphprotocol/graph-network-testnet-phase2"
subgraph_phase3 = "https://api.thegraph.com/subgraphs/name/graphprotocol/graph-testnet-staging-phase3"
subgraph_phase2 = "https://gateway-testnet.thegraph.com/network"
# Overview of Subgraphs with Image, Owner, Id, Description, (Repository)...
subgraphs_query = """
{
  subgraphs {
    id
    displayName
    createdAt
    description
    image
    codeRepository
    website
    withdrawnTokens
    withdrawableTokens
    reserveRatio    
    totalQueryFeesCollected
    totalIndexingRewards
    nameSignalAmount
    unsignalledTokens
    signalledTokens
  }
}
"""

#%%

# Basic Informations about The Graph Network
the_graph_info_query="""
{
  graphNetworks {
    isPaused
    curationPercentage
    protocolFeePercentage
    delegationRatio
    totalTokensStaked
    indexingRewardsPerEpoch
    totalIndexingRewards
    totalQueryFees
    totalSupply
    GRTinUSD
    indexerCount
    delegatorCount
    curatorCount
    subgraphCount
    subgraphDeploymentCount
    GRTinETH
    currentEpoch
    lastLengthUpdateBlock
    maxAllocationEpochs
    totalTokensAllocated
  }
}


"""

#%%
# Get the delpoyed Subgraphs by signalAmount
subgraph_Deployments_by_signal_query = """
{
  subgraphDeployments(orderBy: signalAmount, orderDirection: desc) {
    id
    signalAmount
    originalName
  }
}"""


# %%
# We want to Grab all Subgraph stats
subgraph_deployment_stats = """
{
  subgraphDeployments(orderBy: signalAmount, orderDirection: desc) {
    originalName
    signalAmount    
    stakedTokens
    indexingRewardAmount
    queryFeesAmount
    curatorFeeRewards
    signalledTokens
    queryFeeRebates
    curatorFeeRewards
    signalledTokens
    unsignalledTokens
    reserveRatio
    id    
  }
}"""
# %%
# Get Signals for Subgraph by Curator
subgraph_curator_signal_stats = """
{
  signals(orderBy: id, orderDirection: desc) {
    curator{
      id
    }
    signalledTokens
    unsignalledTokens
    
    lastSignalChange
    realizedRewards
    subgraphDeployment{
      id
    }
  }
}

"""

# get all Curator

curator_list = """
{
  curators{
	id
  totalSignalledTokens
  totalUnsignalledTokens
  totalNameSignalledTokens
  totalNameUnsignalledTokens
  totalWithdrawnTokens
  realizedRewards
  annualizedReturn
  totalReturn
	signalingEfficiency
  totalNameSignal
  totalNameSignalAverageCostBasis
  totalAverageCostBasisPerNameSignal
  }
}

"""

subgraph_list ="""
{
  subgraphDeployments() {
    originalName
    id    
  }
}"""



allocation_list = """

    {
    allocations{
      allocationId:id
      price
      indexer {
        indexerID: id
        url
      }
      subgraphDeployment{
        subgraph_id:id,
        originalName}
      allocatedTokens
      effectiveAllocation
      createdAtEpoch
      closedAtEpoch
      queryFeesCollected
      queryFeeRebates
      indexingRewards
      createdAt
      totalReturn

      
    }
  }

"""
# %%

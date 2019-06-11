#ifndef NtupleMakerPhotonConversions_h
#define NtupleMakerPhotonConversions_h

/* ****************************************** */
/*                                            */
/* Tracker Material with Nuclear Interactions */
/*                                            */
/*               Nicola Pozzobon              */
/*                    2013                    */
/*                                            */
/* ****************************************** */

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
//#include "FWCore/ParameterSet/interface/InputTag.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/ParticleFlowReco/interface/PFDisplacedVertex.h"
#include "DataFormats/ParticleFlowReco/interface/PFDisplacedVertexFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include "DataFormats/Math/interface/deltaPhi.h"

#include "SimTracker/Records/interface/TrackAssociatorRecord.h"
#include "SimDataFormats/TrackingAnalysis/interface/TrackingVertexContainer.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"

#include "SimTracker/Records/interface/TrackAssociatorRecord.h"
//#include "SimTracker/TrackAssociation/interface/ParametersDefinerForTP.h"
//#include "SimTracker/TrackAssociation/interface/TrackAssociatorBase.h" // not exist anymore
#include "TrackAssociatorBase.h"
#include "DataFormats/Common/interface/RefToBaseVector.h"


#include "DataFormats/EgammaCandidates/interface/Conversion.h"
#include "DataFormats/EgammaCandidates/interface/ConversionFwd.h"

#include <TTree.h>
#include <TFile.h>

class NtupleMakerPhotonConversions : public edm::EDAnalyzer
{
  public :
    explicit NtupleMakerPhotonConversions( const edm::ParameterSet& );
    ~NtupleMakerPhotonConversions(){};

  private :
    virtual void beginJob();
//    virtual void beginRun(edm::Run const&, edm::EventSetup const&);
    virtual void analyze( const edm::Event&, const edm::EventSetup& );
    virtual void endJob();

    bool isNuclearInteraction( const TrackingVertex& ) const;
    bool isKaonDecay( const TrackingVertex& ) const;
    bool isConversion( const TrackingVertex& ) const;
    double      VectorParallelR( const TrackingVertex& VecSim, const reco::PFDisplacedVertex& ) const;
    double VectorPerpendicularR( const TrackingVertex&, const reco::PFDisplacedVertex& ) const;

    float getKaonMass( const reco::PFDisplacedVertex& ) const;
    bool isSimVertexOutsideAssCut(const TrackingVertex&, const reco::PFDisplacedVertex&) const;


    //Data members for consumes
    edm::EDGetTokenT<reco::VertexCollection> recoVertexToken;
    edm::EDGetTokenT<std::vector<PileupSummaryInfo>> addPileupInfoToken;
    edm::EDGetTokenT<reco::BeamSpot> offlineBeamSpotToken;
    edm::EDGetTokenT<reco::PFDisplacedVertexCollection> particleFlowDisplacedVertexToken;   
    edm::EDGetTokenT<TrackingVertexCollection> trackingParticlesToken; 
    edm::EDGetTokenT<reco::ConversionCollection> PCToken;
	
    TTree* outputTree;

    /// General
    bool isRealData;
    unsigned int runNumber;
    unsigned int eventNumber;
    unsigned int lumiSection;

    /// Primary vertices
    unsigned int numberOfPV;
    std::vector< double > *PV_x;
    std::vector< double > *PV_y;
    std::vector< double > *PV_z;
    std::vector< double > *PV_xError;
    std::vector< double > *PV_yError;
    std::vector< double > *PV_zError;
    std::vector< bool > *PV_isFake;

    /// MC PileUp
    unsigned int numberOfMC_PUInfo;
    std::vector< unsigned int > *MC_PUInfo_bunchCrossing;
    std::vector< unsigned int > *MC_PUInfo_numberOfInteractions;

    /// BeamSpot
    double BS_x;
    double BS_y;
    double BS_z;
    double BS_zSigma;
    double BS_dxdy;
    double BS_dydz;
    double BS_xWidth;
    double BS_yWidth;

    ///PC Variables
/*    unsigned int numPC{};
    std::vector<double> *PCDV_x;
    std::vector<double> *PCDV_y;
    std::vector<double> *PCDV_z;
    std::vector<double> *PCDV_InvMass;
    std::vector<double> *PCDV_CotTheta;
*/

    /// Tracking Vertices
    unsigned int numberOfMC_TrkV;
    std::vector< bool > *MC_TrkV_isNuclearInteraction;
    std::vector< bool > *MC_TrkV_isKaonDecay;
    std::vector< bool > *MC_TrkV_isConversion;
    std::vector< double > *MC_TrkV_x;
    std::vector< double > *MC_TrkV_y;
    std::vector< double > *MC_TrkV_z;
    std::vector< double > *MC_TrkV_momentumInc_pt;
    std::vector< double > *MC_TrkV_momentumInc_phi;
    std::vector< double > *MC_TrkV_momentumInc_theta;
    std::vector< double > *MC_TrkV_Inc_charge;
    std::vector< int > *MC_TrkV_Inc_pdgId;
    std::vector< double > *MC_TrkV_momentumOut_pt;
    std::vector< double > *MC_TrkV_momentumOut_phi;
    std::vector< double > *MC_TrkV_momentumOut_theta;
    std::vector< double > *MC_TrkV_momentumOut_mass;
    std::vector< unsigned int > *MC_TrkV_numberOfChargedParticles_0p2;
    std::vector< unsigned int > *MC_TrkV_numberOfChargedParticles_0p5;
    std::vector< unsigned int > *MC_TrkV_numberOfChargedParticles_1p0;
    std::vector< unsigned int > *MC_TrkV_numberOfChargedParticles_Out0p2;
    std::vector< unsigned int > *MC_TrkV_numberOfChargedParticles_Out0p5;
    std::vector< unsigned int > *MC_TrkV_numberOfChargedParticles_Out1p0;
    std::vector< bool > *MC_TrkV_isAssociatedPF;
    std::vector< unsigned int > *MC_TrkV_associationPCIdx;
    std::vector< double > *MC_TrkV_associationPC_deltaR2d;
    std::vector< double > *MC_TrkV_associationPC_deltaR3d;
    std::vector< double > *MC_TrkV_associationPC_deltaR3dPerpendicular;
    std::vector< double > *MC_TrkV_associationPC_deltaR3dParallel;
/*
    std::vector< double > *MC_TrkV_associationDeltaPt;
    std::vector< double > *MC_TrkV_associationDeltaPhi;
    std::vector< double > *MC_TrkV_associationDeltaTheta;
    std::vector< double > *MC_TrkV_associationDeltaX;
    std::vector< double > *MC_TrkV_associationDeltaY;
    std::vector< double > *MC_TrkV_associationDeltaZ;
    std::vector< bool > *MC_TrkV_associationIsNuclear;
    std::vector< bool > *MC_TrkV_associationIsNuclearLoose;
    std::vector< bool > *MC_TrkV_associationIsNuclearKink;
    std::vector< bool > *MC_TrkV_associationIsK0;
    std::vector< bool > *MC_TrkV_associationIsLambda;
    std::vector< bool > *MC_TrkV_associationIsLambdaBar;
    std::vector< bool > *MC_TrkV_associationIsKPlusLoose;
    std::vector< bool > *MC_TrkV_associationIsKMinusLoose;
    std::vector< bool > *MC_TrkV_associationIsConversionLoose;
    std::vector< bool > *MC_TrkV_associationIsLooper;
    std::vector< bool > *MC_TrkV_associationIsFake;
    std::vector< bool > *MC_TrkV_associationIsTherePrimaryTrack;
    std::vector< bool > *MC_TrkV_associationIsThereMergedTrack;
*/

    /// Displaced Vertices
    unsigned int numberOfPC;
    std::vector< double > *PC_x;
    std::vector< double > *PC_y;
    std::vector< double > *PC_z;
    std::vector< double > *PC_momentumInc_pt;
    std::vector< double > *PC_Inc_charge;
    std::vector< double > *PC_momentumInc_phi;
    std::vector< double > *PC_momentumInc_theta;
    std::vector< double > *PC_momentumOut_pt;
    std::vector< double > *PC_momentumOut_phi;
    std::vector< double > *PC_momentumOut_theta;
    std::vector< double > *PC_momentumOut_mass;
    std::vector< unsigned int > *PC_momentumOut_numberOfTracks;

	std::vector< double > *PC_fitmomentumOut_pt;
	std::vector< double > *PC_fitmomentumOut_phi;
	std::vector< double > *PC_fitmomentumOut_theta;
	std::vector< double > *PC_fitmomentumOut_mass;

	//added variables from conversions.h  // all of these are calculated according to the original tracks
	std::vector<double> *PC_pairInvariantMass;
	std::vector<double> *PC_pairCotThetaSeparation;
	std::vector<double> *PC_distOfMinimumApproach; //dm variable
	std::vector<double> *PC_dPhiTracksAtVtx; //dphi of tracks evaluate at vertex
	//added variables from vertex.h
	std::vector<double> *PC_vtx_chi2;
	std::vector<double> *PC_vtx_ndof;
	std::vector<double> *PC_vtx_normalizedChi2;
	std::vector<double> *PC_vtx_sigmaxx;
	std::vector<double> *PC_vtx_sigmayy;
	std::vector<double> *PC_vtx_sigmazz;
	std::vector<double> *PC_vtx_sigmaxy;
	std::vector<double> *PC_vtx_sigmaxz;
	std::vector<double> *PC_vtx_sigmayz;

    std::vector< bool > *PC_isNuclear;
    std::vector< bool > *PC_isNuclearLoose;
    std::vector< bool > *PC_isNuclearKink;
    std::vector< bool > *PC_isK0;
    std::vector< bool > *PC_isLambda;
    std::vector< bool > *PC_isLambdaBar;
    std::vector< bool > *PC_isKPlusLoose;
    std::vector< bool > *PC_isKMinusLoose;
    std::vector< bool > *PC_isConversionLoose;
    std::vector< bool > *PC_isLooper;
    std::vector< bool > *PC_isFake;
    std::vector< bool > *PC_isTherePrimaryTrack;
    std::vector< bool > *PC_isThereMergedTrack;
    std::vector< bool > *PC_isAssociatedMC;
    std::vector< double > *PC_deltaR3d_Associated;
    std::vector< double > *PC_deltaR2d_Associated;
    std::vector< unsigned int > *PC_associationMC_TrkVIdx;
    std::vector< std::vector< int > > *PC_vTrack_algo;
    std::vector< std::vector< double > > *PC_vTrack_pt;
    std::vector< std::vector< double > > *PC_vTrack_eta;
    std::vector< std::vector< double > > *PC_vTrack_phi;
    std::vector< std::vector< double > > *PC_vTrack_chi2;
    std::vector< std::vector< double > > *PC_vTrack_normalizedChi2;
    //std::vector< std::vector< bool > > *PC_vTrack_isHighPurity;
    std::vector< std::vector< double > > *PC_vTrack_rho;
    std::vector< std::vector< unsigned int > > *PC_vTrack_numberOfValidHits;
    std::vector< std::vector< unsigned int > > *PC_vTrack_numberOfExpectedOuterHits;
    std::vector< std::vector< unsigned int > > *PC_vTrack_closestDxyPVIdx;
    std::vector< std::vector< double > > *PC_vTrack_closestDxyPVIdx_dxy;
    std::vector< std::vector< double > > *PC_vTrack_closestDxyPVIdx_dz;
    std::vector< std::vector< unsigned int > > *PC_vTrack_closestDzPVIdx;
    std::vector< std::vector< double > > *PC_vTrack_closestDzPVIdx_dxy;
    std::vector< std::vector< double > > *PC_vTrack_closestDzPVIdx_dz;


	//added variables from vertex/conversion/track
	//original track quantites
	std::vector<std::vector<int> > *PC_vTrack_charge;
	//refitted track quantites
	std::vector<std::vector<double> > *PC_fTrack_pt;
	std::vector<std::vector<double> > *PC_fTrack_theta;
	std::vector<std::vector<double> > *PC_fTrack_phi;
	


	unsigned int numberOfPFPC;
};

#endif


/*
Copyright (c) 2018, Wenjia Lu, Zuoqiang Shi, Jian Sun and Bin Wang
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of
conditions and the following disclaimer. Redistributions in binary form must reproduce
the above copyright notice, this list of conditions and the following disclaimer
in the documentation and/or other materials provided with the distribution. 

Neither the name of Tsinghua University nor the names of its contributors
may be used to endorse or promote products derived from this software without specific
prior written permission. 

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO THE IMPLIED WARRANTIES 
OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT
SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
TO, PROCUREMENT OF SUBSTITUTE  GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
DAMAGE.
*/

#ifndef __ReconOctNode_H__
#define __ReconOctNode_H__
#include "Cube.h"
#include <stdio.h>
#include <vector>
#include "Constants.h"

using namespace std;
class ReconOctNode;

struct GridData{
	float value;
	float smoothWidth;
	//float querySmoothWidth;
	// float width;
	GridData* adjacent[Cube::NEIGHBORS];
	long long adjacentKey[Cube::NEIGHBORS];
	float coords[3];
	long long key;
	int maxDepth;
	int minDepth;
	int sampleCalculated;
	bool vectorSet;
	ReconOctNode* node;
	float normalVar;
	GridData(){
		for (int i = 0; i < Cube::NEIGHBORS; i++){
			adjacent[i] = NULL;
			adjacentKey[i] = -1;
		}
		key = -1;
		value = 0;
		coords[0] = coords[1] = coords[2] = 0;
		maxDepth = -1;
		minDepth = DEPTH_LIMIT;
		smoothWidth = 0;
		//querySmoothWidth = 0;
		sampleCalculated = 0;
		node = NULL;
		vectorSet = false;
		normalVar = 0;
	}
};


class NodeAdjacencyFunction{
public:
	virtual void Function(const ReconOctNode* node1) = 0;
};


class ReconOctNode{
private:
	int depth;
	int offset[3];
	
public:
	//long long gridCornerIdx[8];
	GridData* cornerGrid[Cube::CORNERS];
	int gridStartIdx;
	int gridEndIdx;
	vector<int> nodeIdx;
	NormalPoint normalPoint;
	Point barycenter;
	bool hasSample;
	ReconOctNode* parent;
	ReconOctNode* children;
	int normalIdx;
	int mcIdx;
	float centerWeightContribution;
	float value;
private:
	void Index( const int& depth, const int offset[3], int& d, int off[3]);
	const ReconOctNode* __faceNeighbor(const int& dir,const int& off) const;
	const ReconOctNode* __edgeNeighbor(const int& o,const int i[2],const int idx[2]) const;
	ReconOctNode* __faceNeighbor(const int& dir, const int& off, const int& forceChildren);

public:
	ReconOctNode();
	void initChildren();
	void averageNormalPoint(vector<NormalPoint>& np);
	long long getCornerIndex(const int& childNo, const int& maxDepth);
	long long getCornerIndex(const int& childNo, const int& maxDepth) const;
	int leaves();
	int nodes();
	int maxDepth();
	int Depth() const;
	ReconOctNode* nextNode(ReconOctNode* current = NULL);
	ReconOctNode* nextBranch(ReconOctNode* current);
	ReconOctNode* nextLeaf(ReconOctNode* currentLeaf = NULL);
	static int CompareForwardPointerDepths( const void* v1, const void* v2);
	const ReconOctNode* faceNeighbor(const int& faceIndex) const;
	ReconOctNode* faceNeighbor(const int& faceIndex, const int& forceChildren = 0);
	const ReconOctNode* edgeNeighbor(const int& edgeIndex) const;
	void depthAndOffset( int& depth, int off[3]) const;
	void processNodeFaces(ReconOctNode* node, NodeAdjacencyFunction* F, const int& fIndex, const int& processCurrent = 1);
	void __processNodeFaces(ReconOctNode* node, NodeAdjacencyFunction* F, const int& cIndex1, const int& cIndex2, const int& cIndex3, const int& cIndex4);
	void centerAndWidth(float* center, float& width);
};

class SortedNodes{
public:
	ReconOctNode** treeNodes;
	int *nodeCount;
	int maxDepth;
	SortedNodes();
	~SortedNodes();
	void set(ReconOctNode& root, const int& setIndex);
};

class RootInfo{
public:
	const ReconOctNode* node;
	int edgeIndex;
	long long key;
};

class Neighbors{
public:
	ReconOctNode* neighbors[3][3][3];
	Neighbors(void);
	void clear(void);
};

class NeighborKey{
public:
	Neighbors* neighbors;

	NeighborKey(void);
	~NeighborKey(void);

	void set(const int& depth);
	Neighbors& setNeighbors(ReconOctNode* node);
	Neighbors& getNeighbors(ReconOctNode* node);
	
};


#endif
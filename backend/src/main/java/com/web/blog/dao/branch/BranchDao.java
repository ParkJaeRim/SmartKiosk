package com.web.blog.dao.branch;

import java.util.*;

import com.web.blog.model.branch.Branch;
import org.springframework.data.jpa.repository.JpaRepository;

public interface BranchDao extends JpaRepository<Branch, String> {
	List<Branch> findBranchBySid(int sid);
	void deleteByMenuid(int menuid); 
	Branch findByMenuid(int menuid);

	List<Branch> findBranchByMenuid(int menuid);

	Branch findBranchBySidAndMenuid(int sid, int menuid);
	

}
